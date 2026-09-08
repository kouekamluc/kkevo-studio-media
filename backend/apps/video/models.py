import uuid
from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel

class VideoStory(TimeStampedModel):
    class VideoType(models.TextChoices):
        SHORT_REEL = 'SHORT_REEL', '60 Seconds of Context (Reel)'
        EXPLAINER = 'EXPLAINER', 'Video Explainer (5-10 min)'
        DOCUMENTARY = 'DOCUMENTARY', 'Documentary Feature (Longform)'
        INTERVIEW = 'INTERVIEW', 'Diplomatic & Economic Interview'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, db_index=True)
    summary = models.TextField(blank=True)
    video_type = models.CharField(max_length=32, choices=VideoType.choices, default=VideoType.EXPLAINER, db_index=True)
    video_url = models.URLField(help_text="Direct MP4, YouTube, or HLS stream URL")
    thumbnail_url = models.URLField(blank=True)
    duration_seconds = models.PositiveIntegerField(default=180, help_text="Duration in seconds")
    transcript = models.TextField(blank=True, help_text="Full transcribed speech for accessibility and SEO")
    is_featured = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    related_article = models.ForeignKey(
        'articles.Article',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='video_stories'
    )
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:260]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.get_video_type_display()}] {self.title}"
