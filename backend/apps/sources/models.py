import uuid
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel

class SourceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=40, unique=True, help_text="e.g. GOV_OFFICIAL, WIRE_REUTERS_AP, ACADEMIC")
    description = models.TextField(blank=True)
    default_credibility_tier = models.IntegerField(default=1, help_text="1=Primary/Direct, 2=Secondary Wire, 3=Unofficial")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Source(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, help_text="Headline or Title of Document/Report")
    publisher = models.CharField(max_length=150, help_text="e.g. Ministry of Mines DRC, Reuters, African Union, USGS")
    url = models.URLField(max_length=500, blank=True)
    archived_url = models.URLField(max_length=500, blank=True, help_text="Wayback Machine or archive link")
    source_type = models.ForeignKey(SourceType, on_delete=models.PROTECT, related_name='sources')
    author = models.CharField(max_length=150, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    accessed_date = models.DateField(null=True, blank=True)
    reliability_notes = models.TextField(blank=True, help_text="Internal assessment of the publisher and methodology")
    internal_notes = models.TextField(blank=True, help_text="Private newsroom fact-checking notes")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.publisher})"

class Citation(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='citations')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='citations')
    citation_number = models.PositiveIntegerField(default=1)
    quote_excerpt = models.TextField(blank=True, help_text="Exact excerpt cited from the source")
    public_label = models.CharField(max_length=100, blank=True, help_text="e.g. 'Paragraph 14, IMF Country Report No. 24/89'")
    page_or_timestamp = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ['citation_number']
        unique_together = ('article', 'citation_number')

    def __str__(self):
        return f"Citation [{self.citation_number}] on {self.article_id}: {self.source.title}"

class Claim(TimeStampedModel):
    class VerificationStatus(models.TextChoices):
        VERIFIED_FACT = 'VERIFIED_FACT', 'Verified Fact'
        OFFICIAL_CLAIM = 'OFFICIAL_CLAIM', 'Official Claim / State Statement'
        ALLEGATION = 'ALLEGATION', 'Allegation / Third-Party Report'
        DISPUTED = 'DISPUTED', 'Disputed Claim'
        UNVERIFIED = 'UNVERIFIED', 'Unverified / Developing'
        ANALYSIS = 'ANALYSIS', 'Editorial Analysis / Synthesis'
        OPINION = 'OPINION', 'Perspective / Commentary'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='claims')
    claim_text = models.TextField(help_text="Key assertion scrutinized")
    verification_status = models.CharField(
        max_length=32,
        choices=VerificationStatus.choices,
        default=VerificationStatus.VERIFIED_FACT,
        db_index=True
    )
    verification_notes = models.TextField(blank=True, help_text="Editorial explanation of how this was audited")
    primary_source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_claims')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"[{self.get_verification_status_display()}] {self.claim_text[:60]}..."

class Correction(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='corrections')
    title = models.CharField(max_length=255, help_text="Summary of what was corrected")
    original_claim = models.TextField()
    corrected_claim = models.TextField()
    reason_for_correction = models.TextField(help_text="Detailed explanation of error, origin, and corrective action")
    corrected_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    corrected_at = models.DateTimeField(auto_now_add=True)
    is_public_banner_active = models.BooleanField(default=True, help_text="Displays a red correction banner at the top of the article")

    class Meta:
        ordering = ['-corrected_at']

    def __str__(self):
        return f"Correction on {self.article_id}: {self.title}"
