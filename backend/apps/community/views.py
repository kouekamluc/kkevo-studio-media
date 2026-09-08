from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import ReaderBookmark, Comment
from .serializers import ReaderBookmarkSerializer, CommentSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderBookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReaderBookmark.objects.filter(user=self.request.user).select_related('article')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        article_id = self.request.query_params.get('article')
        qs = Comment.objects.filter(status=Comment.Status.APPROVED)
        if article_id:
            qs = qs.filter(article_id=article_id)
        return qs

    def perform_create(self, serializer):
        # Auto-approve comments by staff, otherwise pending
        is_staff = self.request.user.is_editorial_staff()
        initial_status = Comment.Status.APPROVED if is_staff else Comment.Status.PENDING
        serializer.save(user=self.request.user, status=initial_status)
