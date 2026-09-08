from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q, F
from .models import Article, ArticleRevision
from .serializers import (
    ArticleListSerializer, ArticleDetailSerializer,
    ArticleEditorialSerializer, ArticleRevisionSerializer
)
from apps.core.permissions import IsEditorOrReadOnly, IsAuthorOrEditor
from apps.live.models import BreakingAlert

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleListSerializer

    def get_queryset(self):
        # Public readers only see published or corrected stories
        qs = Article.objects.filter(
            status__in=[Article.Status.PUBLISHED, Article.Status.CORRECTED]
        ).select_related('category', 'country', 'hero_image').prefetch_related('authors')

        # Filters
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category__slug=category)

        country = self.request.query_params.get('country')
        if country:
            qs = qs.filter(country__slug=country)

        topic = self.request.query_params.get('topic')
        if topic:
            qs = qs.filter(topics__slug=topic)

        content_type = self.request.query_params.get('type')
        if content_type:
            qs = qs.filter(content_type=content_type)

        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(subtitle__icontains=q) |
                Q(summary__icontains=q) |
                Q(body__icontains=q)
            )

        return qs.order_by('-published_at')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment views atomically
        Article.objects.filter(id=instance.id).update(views_count=F('views_count') + 1)
        instance.refresh_from_db(fields=['views_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def breaking(self, request):
        """Return the active breaking alert or breaking story."""
        alert = BreakingAlert.objects.filter(is_active=True).order_by('-priority', '-published_at').first()
        if alert:
            return Response({
                'id': alert.id,
                'headline': alert.headline,
                'target_url': alert.target_url,
                'priority': alert.priority,
                'published_at': alert.published_at,
            })
        # Fallback to most recent breaking article
        story = Article.objects.filter(
            status=Article.Status.PUBLISHED, is_breaking=True
        ).order_by('-published_at').first()
        if story:
            return Response({
                'id': story.id,
                'headline': story.short_title or story.title,
                'target_url': f"/article/{story.slug}",
                'priority': 1,
                'published_at': story.published_at,
            })
        return Response(None)

class HomepageView(views.APIView):
    """
    Optimized consolidated homepage feed delivering:
    - Hero lead story
    - Secondary lead stories
    - Latest chronological news
    - KKEVO Analysis stories
    - KKEVO Explainers
    - Resource / Industrialization focus
    - History / Archive spotlight
    - Video stories
    - Most read
    - Breaking banner
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        base_qs = Article.objects.filter(
            status__in=[Article.Status.PUBLISHED, Article.Status.CORRECTED]
        ).select_related('category', 'country', 'hero_image').prefetch_related('authors')

        # Hero story (either marked featured or newest analysis/lead)
        hero = base_qs.filter(is_featured=True).order_by('-published_at').first()
        if not hero:
            hero = base_qs.order_by('-published_at').first()

        hero_id = hero.id if hero else None

        # Secondary leads (exclude hero)
        secondary = base_qs.exclude(id=hero_id).order_by('-published_at')[:4]

        # Latest News stream
        latest_news = base_qs.filter(content_type=Article.ContentType.NEWS).order_by('-published_at')[:8]

        # Analysis section
        analysis = base_qs.filter(content_type=Article.ContentType.ANALYSIS).order_by('-published_at')[:4]

        # Explainers
        explainers = base_qs.filter(content_type=Article.ContentType.EXPLAINER).order_by('-published_at')[:4]

        # Resources & Industrialisation
        resources = base_qs.filter(
            Q(category__slug='resources') | Q(topics__slug='critical-minerals') | Q(topics__slug='industrialisation')
        ).distinct().order_by('-published_at')[:4]

        # History spotlight
        history = base_qs.filter(
            Q(category__slug='history') | Q(content_type=Article.ContentType.HISTORY)
        ).order_by('-published_at')[:3]

        # Most read stories
        most_read = base_qs.order_by('-views_count', '-published_at')[:5]

        # Breaking alert
        alert = BreakingAlert.objects.filter(is_active=True).order_by('-priority', '-published_at').first()

        context = {'request': request}
        return Response({
            'breaking': {
                'headline': alert.headline,
                'target_url': alert.target_url,
                'priority': alert.priority,
                'published_at': alert.published_at,
            } if alert else None,
            'hero': ArticleListSerializer(hero, context=context).data if hero else None,
            'secondary_leads': ArticleListSerializer(secondary, many=True, context=context).data,
            'latest_news': ArticleListSerializer(latest_news, many=True, context=context).data,
            'analysis': ArticleListSerializer(analysis, many=True, context=context).data,
            'explainers': ArticleListSerializer(explainers, many=True, context=context).data,
            'resources': ArticleListSerializer(resources, many=True, context=context).data,
            'history': ArticleListSerializer(history, many=True, context=context).data,
            'most_read': ArticleListSerializer(most_read, many=True, context=context).data,
        })

class EditorialArticleViewSet(viewsets.ModelViewSet):
    """Newsroom CMS workflow viewset for contributors, editors, and admins."""
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleEditorialSerializer
    permission_classes = [IsAuthorOrEditor]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Article.objects.none()
        if user.role in ['EDITOR', 'SENIOR_EDITOR', 'ADMIN']:
            return Article.objects.all().order_by('-created_at')
        # Contributors only see their own stories
        if hasattr(user, 'author_profile'):
            return Article.objects.filter(authors=user.author_profile).order_by('-created_at')
        return Article.objects.none()

    @action(detail=True, methods=['post'], permission_classes=[IsEditorOrReadOnly])
    def transition_status(self, request, pk=None):
        article = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(Article.Status.choices):
            return Response({'error': 'Invalid status transition.'}, status=status.HTTP_400_BAD_REQUEST)
        article.status = new_status
        article.save()
        return Response({'status': article.status, 'message': f'Article status updated to {new_status}'})
