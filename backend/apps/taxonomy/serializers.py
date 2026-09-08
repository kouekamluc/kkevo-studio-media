from rest_framework import serializers
from .models import Category, Subcategory, Topic, Region, Country

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'description']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'order', 'is_nav_visible', 'color_accent', 'subcategories']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'slug', 'description', 'is_featured', 'icon_name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'code', 'description']

class CountrySerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = Country
        fields = [
            'id', 'name', 'slug', 'iso_code', 'region', 'region_name',
            'capital', 'flag_emoji', 'gdp_nominal_usd', 'population',
            'strategic_resources', 'sovereignty_notes', 'latitude', 'longitude', 'is_featured'
        ]
