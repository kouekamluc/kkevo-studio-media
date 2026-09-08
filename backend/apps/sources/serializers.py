from rest_framework import serializers
from .models import SourceType, Source, Citation, Claim, Correction

class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceType
        fields = ['id', 'name', 'code', 'description', 'default_credibility_tier']

class SourceSerializer(serializers.ModelSerializer):
    source_type_name = serializers.CharField(source='source_type.name', read_only=True)

    class Meta:
        model = Source
        fields = [
            'id', 'title', 'publisher', 'url', 'archived_url', 'source_type',
            'source_type_name', 'author', 'publication_date', 'accessed_date',
            'reliability_notes', 'created_at'
        ]

class CitationSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)
    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Source.objects.all(), source='source', write_only=True
    )

    class Meta:
        model = Citation
        fields = ['id', 'article', 'source', 'source_id', 'citation_number', 'quote_excerpt', 'public_label', 'page_or_timestamp']

class ClaimSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_verification_status_display', read_only=True)
    primary_source = SourceSerializer(read_only=True)

    class Meta:
        model = Claim
        fields = [
            'id', 'article', 'claim_text', 'verification_status',
            'status_display', 'verification_notes', 'primary_source', 'created_at'
        ]

class CorrectionSerializer(serializers.ModelSerializer):
    corrected_by_name = serializers.CharField(source='corrected_by.get_full_name', read_only=True)
    article_title = serializers.CharField(source='article.title', read_only=True)
    article_slug = serializers.CharField(source='article.slug', read_only=True)

    class Meta:
        model = Correction
        fields = [
            'id', 'article', 'article_title', 'article_slug', 'title', 'original_claim',
            'corrected_claim', 'reason_for_correction', 'corrected_by_name',
            'corrected_at', 'is_public_banner_active'
        ]
