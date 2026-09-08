import uuid
import math
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from apps.core.models import TimeStampedModel

class Article(TimeStampedModel):
    class ContentType(models.TextChoices):
        NEWS = 'NEWS', 'News (Fast Verified)'
        ANALYSIS = 'ANALYSIS', 'Analysis (Interpretation & Implication)'
        EXPLAINER = 'EXPLAINER', 'Explainer (Deep Educational Breakdown)'
        HISTORY = 'HISTORY', 'History & Pre-Colonial Archive'
        DATA = 'DATA', 'Data & Resource Journalism'
        VIDEO = 'VIDEO', 'Video & Short Documentary'
        DEBATE = 'DEBATE', 'Debate & Structured Perspective'
        INVESTIGATION = 'INVESTIGATION', 'Investigative Report'

    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        SUBMITTED = 'SUBMITTED', 'Submitted for Review'
        IN_REVIEW = 'IN_REVIEW', 'Under Editor Review'
        FACT_CHECK = 'FACT_CHECK', 'Fact Check & Source Audit'
        APPROVED = 'APPROVED', 'Approved for Publication'
        SCHEDULED = 'SCHEDULED', 'Scheduled'
        PUBLISHED = 'PUBLISHED', 'Published'
        CORRECTED = 'CORRECTED', 'Published with Correction'
        ARCHIVED = 'ARCHIVED', 'Archived'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True)
    short_title = models.CharField(max_length=120, blank=True, help_text="Concise headline for mobile tickers and breaking bar")
    slug = models.SlugField(max_length=280, unique=True, db_index=True)
    subtitle = models.CharField(max_length=350, blank=True, help_text="Dek / Sub-headline providing immediate context")
    summary = models.TextField(blank=True, help_text="Executive summary for syndication, SEO, and card previews")
    content_type = models.CharField(max_length=32, choices=ContentType.choices, default=ContentType.NEWS, db_index=True)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.DRAFT, db_index=True)

    body = models.TextField(help_text="Full article text in Markdown / HTML formatting")
    structured_blocks = models.JSONField(
        default=list,
        blank=True,
        help_text="Interactive structured blocks: pull quotes, key facts boxes, timelines, data charts"
    )

    hero_image = models.ForeignKey(
        'media_library.MediaAsset',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles_as_hero'
    )
    hero_image_url = models.URLField(blank=True, help_text="Direct hero image URL fallback")
    hero_caption = models.TextField(blank=True)
    hero_credit = models.CharField(max_length=200, blank=True)
    hero_video_url = models.URLField(blank=True, help_text="YouTube, Vimeo, or MP4 URL if lead story is video")

    category = models.ForeignKey('taxonomy.Category', on_delete=models.PROTECT, related_name='articles')
    subcategory = models.ForeignKey('taxonomy.Subcategory', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    region = models.ForeignKey('taxonomy.Region', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    country = models.ForeignKey('taxonomy.Country', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    topics = models.ManyToManyField('taxonomy.Topic', blank=True, related_name='articles')

    authors = models.ManyToManyField('authors.AuthorProfile', related_name='articles')
    primary_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='edited_articles'
    )

    published_at = models.DateTimeField(null=True, blank=True, db_index=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    reading_time_minutes = models.PositiveIntegerField(default=3)

    is_featured = models.BooleanField(default=False, db_index=True, help_text="Featured on homepage top module")
    is_breaking = models.BooleanField(default=False, db_index=True, help_text="Featured in breaking news ticker")
    is_sensitive = models.BooleanField(default=False, help_text="Requires Senior Editor / Legal review")
    views_count = models.PositiveIntegerField(default=0)
    bookmarks_count = models.PositiveIntegerField(default=0)

    # SEO & Social Syndication
    seo_title = models.CharField(max_length=160, blank=True)
    seo_description = models.CharField(max_length=255, blank=True)
    canonical_url = models.URLField(blank=True)

    internal_editorial_notes = models.TextField(blank=True, help_text="Newsroom internal collaboration and desk notes")

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['content_type', '-published_at']),
            models.Index(fields=['category', '-published_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug[:260]
        # Calculate reading time based on 200 words/minute
        words = len(self.body.split()) if self.body else 0
        self.reading_time_minutes = max(1, math.ceil(words / 200))
        # Auto-set published_at when published
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.get_content_type_display()}] {self.title}"

class ArticleRevision(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='revisions')
    revision_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=350, blank=True)
    body = models.TextField()
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    diff_summary = models.TextField(blank=True)

    class Meta:
        ordering = ['-revision_number']
        unique_together = ('article', 'revision_number')

    def __str__(self):
        return f"Revision {self.revision_number} for {self.article.title}"
