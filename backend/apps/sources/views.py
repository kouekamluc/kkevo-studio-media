from rest_framework import viewsets, permissions
from .models import SourceType, Source, Citation, Claim, Correction
from .serializers import SourceTypeSerializer, SourceSerializer, CitationSerializer, ClaimSerializer, CorrectionSerializer

class SourceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.select_related('source_type').all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'publisher', 'author']

class CitationViewSet(viewsets.ModelViewSet):
    queryset = Citation.objects.select_related('source', 'article').all()
    serializer_class = CitationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        article_id = self.request.query_params.get('article')
        if article_id:
            qs = qs.filter(article_id=article_id)
        return qs

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.select_related('primary_source', 'article').all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        article_id = self.request.query_params.get('article')
        if article_id:
            qs = qs.filter(article_id=article_id)
        return qs

class CorrectionViewSet(viewsets.ModelViewSet):
    queryset = Correction.objects.select_related('article', 'corrected_by').all()
    serializer_class = CorrectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        article_id = self.request.query_params.get('article')
        if article_id:
            qs = qs.filter(article_id=article_id)
        return qs
