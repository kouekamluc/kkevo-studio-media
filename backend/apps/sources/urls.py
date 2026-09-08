from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SourceTypeViewSet, SourceViewSet, CitationViewSet, ClaimViewSet, CorrectionViewSet

router = DefaultRouter()
router.register(r'source-types', SourceTypeViewSet, basename='source-type')
router.register(r'sources', SourceViewSet, basename='source')
router.register(r'citations', CitationViewSet, basename='citation')
router.register(r'claims', ClaimViewSet, basename='claim')
router.register(r'corrections', CorrectionViewSet, basename='correction')

urlpatterns = [
    path('', include(router.urls)),
]
