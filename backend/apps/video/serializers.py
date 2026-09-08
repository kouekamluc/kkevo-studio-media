from rest_framework import serializers
from .models import VideoStory

class VideoStorySerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_video_type_display', read_only=True)
    formatted_duration = serializers.SerializerMethodField()

    class Meta:
        model = VideoStory
        fields = [
            'id', 'title', 'slug', 'summary', 'video_type', 'type_display',
            'video_url', 'thumbnail_url', 'duration_seconds', 'formatted_duration',
            'transcript', 'is_featured', 'views_count', 'related_article',
            'published_at'
        ]

    def get_formatted_duration(self, obj):
        minutes = obj.duration_seconds // 60
        seconds = obj.duration_seconds % 60
        return f"{minutes}:{seconds:02d}"
