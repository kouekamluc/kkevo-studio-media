from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
