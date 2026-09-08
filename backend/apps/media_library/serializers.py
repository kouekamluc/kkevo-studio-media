from rest_framework import serializers
from .models import MediaAsset

class MediaAssetSerializer(serializers.ModelSerializer):
    effective_url = serializers.SerializerMethodField()
    classification_display = serializers.CharField(source='get_classification_display', read_only=True)

    class Meta:
        model = MediaAsset
        fields = [
            'id', 'title', 'effective_url', 'asset_type', 'classification',
            'classification_display', 'alt_text', 'caption', 'credit',
            'source_organization', 'copyright_notice', 'date_captured',
            'location', 'created_at'
        ]

    def get_effective_url(self, obj):
        if obj.file:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.file.url) if request else obj.file.url
        return obj.external_url or ''
