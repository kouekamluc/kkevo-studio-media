import uuid
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel

class MediaAsset(TimeStampedModel):
    class AssetType(models.TextChoices):
        IMAGE = 'IMAGE', 'Image'
        VIDEO = 'VIDEO', 'Video'
        AUDIO = 'AUDIO', 'Audio'
        DOCUMENT = 'DOCUMENT', 'Document / PDF'

    class Classification(models.TextChoices):
        OFFICIAL_PHOTO = 'OFFICIAL_PHOTO', 'Official Photograph'
        LICENSED_WIRE = 'LICENSED_WIRE', 'Licensed Wire / Agency'
        STAFF_PHOTO = 'STAFF_PHOTO', 'Staff / Commissioned Photo'
        ARCHIVAL = 'ARCHIVAL', 'Archival / Historical Record'
        INFOGRAPHIC = 'INFOGRAPHIC', 'Editorial Graphic / Map / Chart'
        AI_ILLUSTRATION = 'AI_ILLUSTRATION', 'AI-Generated Conceptual Illustration (Non-Documentary)'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_library/%Y/%m/', null=True, blank=True)
    external_url = models.URLField(blank=True, help_text="Direct CDN/External URL fallback")
    asset_type = models.CharField(max_length=20, choices=AssetType.choices, default=AssetType.IMAGE)
    classification = models.CharField(max_length=30, choices=Classification.choices, default=Classification.STAFF_PHOTO)
    alt_text = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    credit = models.CharField(max_length=200, help_text="e.g. AFP / Getty Images or KKEVO Field Unit")
    source_organization = models.CharField(max_length=150, blank=True)
    copyright_notice = models.CharField(max_length=200, blank=True)
    date_captured = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=150, blank=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_classification_display()})"
