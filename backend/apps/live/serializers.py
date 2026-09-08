from rest_framework import serializers
from .models import BreakingAlert, LiveBlog, LiveUpdate
from apps.authors.serializers import AuthorProfileSerializer

class BreakingAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakingAlert
        fields = ['id', 'headline', 'target_url', 'priority', 'is_active', 'published_at']

class LiveUpdateSerializer(serializers.ModelSerializer):
    author = AuthorProfileSerializer(read_only=True)

    class Meta:
        model = LiveUpdate
        fields = ['id', 'headline', 'content', 'author', 'timestamp', 'is_pinned', 'image_url']

class LiveBlogListSerializer(serializers.ModelSerializer):
    updates_count = serializers.IntegerField(source='updates.count', read_only=True)

    class Meta:
        model = LiveBlog
        fields = ['id', 'title', 'slug', 'summary', 'status', 'cover_image_url', 'started_at', 'ended_at', 'updates_count']

class LiveBlogDetailSerializer(serializers.ModelSerializer):
    updates = LiveUpdateSerializer(many=True, read_only=True)

    class Meta:
        model = LiveBlog
        fields = ['id', 'title', 'slug', 'summary', 'status', 'cover_image_url', 'started_at', 'ended_at', 'updates']
