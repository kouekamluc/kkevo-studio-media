from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TopicViewSet, CountryViewSet, RegionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'regions', RegionViewSet, basename='region')

urlpatterns = [
    path('', include(router.urls)),
]
