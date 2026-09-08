import uuid
from django.db import models
from apps.core.models import TimeStampedModel

class NewsletterSubscriber(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    preferences = models.JSONField(
        default=dict,
        help_text="Tracks subscriptions: daily_briefing, weekly_analysis, critical_minerals, geopolitics"
    )
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.email} (Active: {self.is_active})"
