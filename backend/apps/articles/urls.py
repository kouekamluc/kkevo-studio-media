from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, HomepageView, EditorialArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'editorial/articles', EditorialArticleViewSet, basename='editorial-article')

urlpatterns = [
    path('homepage/', HomepageView.as_view(), name='homepage-feed'),
    path('articles/homepage/', HomepageView.as_view(), name='articles-homepage-feed'),
    path('', include(router.urls)),
]
