import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from apps.core.models import TimeStampedModel

class BreakingAlert(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=255)
    target_url = models.CharField(max_length=255, blank=True)
    priority = models.PositiveIntegerField(default=1, help_text="Higher priority appears first")
    is_active = models.BooleanField(default=True, db_index=True)
    published_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-priority', '-published_at']

    def __str__(self):
        return f"[BREAKING] {self.headline}"

class LiveBlog(TimeStampedModel):
    class Status(models.TextChoices):
        LIVE = 'LIVE', 'Live Updates Active'
        PAUSED = 'PAUSED', 'Temporarily Paused'
        CONCLUDED = 'CONCLUDED', 'Live Coverage Concluded'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, db_index=True)
    summary = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.LIVE)
    cover_image_url = models.URLField(blank=True)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-started_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:260]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.status}] {self.title}"

class LiveUpdate(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    live_blog = models.ForeignKey(LiveBlog, on_delete=models.CASCADE, related_name='updates')
    headline = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('authors.AuthorProfile', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    is_pinned = models.BooleanField(default=False)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-is_pinned', '-timestamp']

    def __str__(self):
        return f"{self.headline} ({self.timestamp.strftime('%H:%M')})"
