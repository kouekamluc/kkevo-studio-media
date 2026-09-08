from rest_framework import serializers
from .models import NewsletterSubscriber

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['id', 'email', 'preferences', 'is_active', 'created_at']
        read_only_fields = ['id', 'is_active', 'created_at']

    def create(self, validated_data):
        email = validated_data.get('email').lower().strip()
        default_prefs = {
            'daily_briefing': True,
            'weekly_analysis': True,
            'critical_minerals': True,
            'geopolitics': True,
        }
        preferences = validated_data.get('preferences') or default_prefs
        subscriber, created = NewsletterSubscriber.objects.update_or_create(
            email=email,
            defaults={'is_active': True, 'preferences': preferences}
        )
        return subscriber
