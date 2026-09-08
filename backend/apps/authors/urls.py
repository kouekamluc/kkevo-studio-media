from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorProfileViewSet

router = DefaultRouter()
router.register(r'authors', AuthorProfileViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
