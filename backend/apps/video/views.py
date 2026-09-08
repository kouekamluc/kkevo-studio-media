from rest_framework import viewsets, permissions
from .models import VideoStory
from .serializers import VideoStorySerializer

class VideoStoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoStory.objects.all()
    serializer_class = VideoStorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        video_type = self.request.query_params.get('type')
        if video_type:
            qs = qs.filter(video_type=video_type)
        featured = self.request.query_params.get('featured')
        if featured and featured.lower() in ['1', 'true']:
            qs = qs.filter(is_featured=True)
        return qs
