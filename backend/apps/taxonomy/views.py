from rest_framework import viewsets, permissions
from .models import Category, Topic, Region, Country
from .serializers import CategorySerializer, TopicSerializer, RegionSerializer, CountrySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.prefetch_related('subcategories').all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    pagination_class = None

class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    pagination_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        featured_only = self.request.query_params.get('featured')
        if featured_only and featured_only.lower() in ['1', 'true']:
            return qs.filter(is_featured=True)
        return qs

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.select_related('region').all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    pagination_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        region = self.request.query_params.get('region')
        if region:
            qs = qs.filter(region__code=region)
        return qs

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
