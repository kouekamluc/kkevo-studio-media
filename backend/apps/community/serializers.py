from rest_framework import serializers
from .models import ReaderBookmark, TopicFollow, Comment
from apps.articles.serializers import ArticleListSerializer

class ReaderBookmarkSerializer(serializers.ModelSerializer):
    article_data = ArticleListSerializer(source='article', read_only=True)

    class Meta:
        model = ReaderBookmark
        fields = ['id', 'article', 'article_data', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user_name', 'content', 'created_at']
        read_only_fields = ['id', 'user_name', 'created_at']
