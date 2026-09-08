from rest_framework import views, permissions
from rest_framework.response import Response
from apps.articles.models import Article
from apps.sources.models import Correction
from apps.newsletter.models import NewsletterSubscriber

class NewsroomStatsView(views.APIView):
    """Aggregated editorial stats for newsroom editors and managers."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_published = Article.objects.filter(status=Article.Status.PUBLISHED).count()
        total_drafts = Article.objects.filter(status=Article.Status.DRAFT).count()
        in_review = Article.objects.filter(status=Article.Status.IN_REVIEW).count()
        fact_check_queue = Article.objects.filter(status=Article.Status.FACT_CHECK).count()
        active_corrections = Correction.objects.filter(is_public_banner_active=True).count()
        subscribers = NewsletterSubscriber.objects.filter(is_active=True).count()

        top_articles = Article.objects.filter(
            status=Article.Status.PUBLISHED
        ).order_by('-views_count')[:5].values('title', 'slug', 'views_count', 'published_at')

        return Response({
            'published_count': total_published,
            'drafts_count': total_drafts,
            'in_review_count': in_review,
            'fact_check_count': fact_check_queue,
            'active_corrections': active_corrections,
            'total_subscribers': subscribers,
            'top_articles': list(top_articles)
        })
