from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreakingAlertViewSet, LiveBlogViewSet

router = DefaultRouter()
router.register(r'breaking-alerts', BreakingAlertViewSet, basename='breaking-alert')
router.register(r'live-blogs', LiveBlogViewSet, basename='live-blog')

urlpatterns = [
    path('', include(router.urls)),
]
