from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoStoryViewSet

router = DefaultRouter()
router.register(r'videos', VideoStoryViewSet, basename='video')

urlpatterns = [
    path('', include(router.urls)),
]
