import uuid
from django.db import models
from apps.core.models import TimeStampedModel

class PageView(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=255, db_index=True)
    article = models.ForeignKey('articles.Article', on_delete=models.SET_NULL, null=True, blank=True)
    referrer = models.CharField(max_length=255, blank=True)
    country_iso = models.CharField(max_length=3, blank=True)
    read_percentage = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
