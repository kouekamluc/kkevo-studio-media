from rest_framework import serializers
from .models import Article, ArticleRevision
from apps.taxonomy.serializers import CategorySerializer, TopicSerializer, CountrySerializer, RegionSerializer
from apps.authors.serializers import AuthorProfileSerializer
from apps.sources.serializers import CitationSerializer, ClaimSerializer, CorrectionSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True, default='')
    country_flag = serializers.CharField(source='country.flag_emoji', read_only=True, default='')
    country_slug = serializers.CharField(source='country.slug', read_only=True, default='')
    authors = AuthorProfileSerializer(many=True, read_only=True)
    content_type_display = serializers.CharField(source='get_content_type_display', read_only=True)
    effective_hero_image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'short_title', 'slug', 'subtitle', 'summary',
            'content_type', 'content_type_display', 'status',
            'category_name', 'category_slug', 'country_name', 'country_flag', 'country_slug',
            'authors', 'effective_hero_image', 'hero_caption', 'hero_credit',
            'published_at', 'reading_time_minutes', 'is_featured', 'is_breaking',
            'views_count'
        ]

    def get_effective_hero_image(self, obj):
        if obj.hero_image:
            if obj.hero_image.file:
                request = self.context.get('request')
                return request.build_absolute_uri(obj.hero_image.file.url) if request else obj.hero_image.file.url
            return obj.hero_image.external_url or ''
        return obj.hero_image_url or ''

class ArticleDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    topics = TopicSerializer(many=True, read_only=True)
    authors = AuthorProfileSerializer(many=True, read_only=True)
    citations = CitationSerializer(many=True, read_only=True)
    claims = ClaimSerializer(many=True, read_only=True)
    corrections = CorrectionSerializer(many=True, read_only=True)
    content_type_display = serializers.CharField(source='get_content_type_display', read_only=True)
    effective_hero_image = serializers.SerializerMethodField()
    active_correction = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'short_title', 'slug', 'subtitle', 'summary',
            'content_type', 'content_type_display', 'status', 'body', 'structured_blocks',
            'category', 'country', 'region', 'topics', 'authors',
            'effective_hero_image', 'hero_caption', 'hero_credit', 'hero_video_url',
            'published_at', 'updated_at', 'reading_time_minutes',
            'is_featured', 'is_breaking', 'is_sensitive',
            'seo_title', 'seo_description', 'canonical_url',
            'citations', 'claims', 'corrections', 'active_correction',
            'views_count', 'bookmarks_count'
        ]

    def get_effective_hero_image(self, obj):
        if obj.hero_image:
            if obj.hero_image.file:
                request = self.context.get('request')
                return request.build_absolute_uri(obj.hero_image.file.url) if request else obj.hero_image.file.url
            return obj.hero_image.external_url or ''
        return obj.hero_image_url or ''

    def get_active_correction(self, obj):
        active = obj.corrections.filter(is_public_banner_active=True).first()
        if active:
            return CorrectionSerializer(active).data
        return None

class ArticleEditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleRevisionSerializer(serializers.ModelSerializer):
    changed_by_name = serializers.CharField(source='changed_by.get_full_name', read_only=True)

    class Meta:
        model = ArticleRevision
        fields = ['id', 'revision_number', 'title', 'subtitle', 'body', 'changed_by_name', 'diff_summary', 'created_at']
