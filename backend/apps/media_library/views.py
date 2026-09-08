from rest_framework import viewsets, permissions
from .models import MediaAsset
from .serializers import MediaAssetSerializer

class MediaAssetViewSet(viewsets.ModelViewSet):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        asset_type = self.request.query_params.get('type')
        if asset_type:
            qs = qs.filter(asset_type=asset_type)
        return qs
