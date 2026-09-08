from rest_framework import viewsets, permissions
from .models import BreakingAlert, LiveBlog, LiveUpdate
from .serializers import BreakingAlertSerializer, LiveBlogListSerializer, LiveBlogDetailSerializer, LiveUpdateSerializer

class BreakingAlertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BreakingAlert.objects.filter(is_active=True)
    serializer_class = BreakingAlertSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class LiveBlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiveBlog.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LiveBlogDetailSerializer
        return LiveBlogListSerializer
