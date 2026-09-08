from rest_framework import serializers
from .models import AuthorProfile

class AuthorProfileSerializer(serializers.ModelSerializer):
    effective_avatar = serializers.SerializerMethodField()

    class Meta:
        model = AuthorProfile
        fields = [
            'id', 'display_name', 'slug', 'editorial_title', 'bio',
            'effective_avatar', 'twitter_handle', 'linkedin_url',
            'location', 'is_verified', 'joined_date'
        ]

    def get_effective_avatar(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.avatar.url) if request else obj.avatar.url
        return obj.avatar_url or ''
