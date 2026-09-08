import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify

class AuthorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_profile'
    )
    display_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, db_index=True)
    editorial_title = models.CharField(max_length=120, default='Contributing Editor', help_text="e.g. Senior Geopolitical Analyst, Energy Reporter")
    bio = models.TextField()
    avatar = models.ImageField(upload_to='authors/', null=True, blank=True)
    avatar_url = models.URLField(blank=True, help_text="Direct URL fallback for avatar image")
    twitter_handle = models.CharField(max_length=64, blank=True)
    linkedin_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True, help_text="e.g. Kinshasa, DRC or Accra, Ghana")
    is_verified = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.display_name or self.user.get_full_name() or self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.display_name} ({self.editorial_title})"
