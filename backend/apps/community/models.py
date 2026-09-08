import uuid
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel

class ReaderBookmark(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='bookmarked_by')

    class Meta:
        unique_together = ('user', 'article')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} saved {self.article.title}"

class TopicFollow(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_topics')
    topic = models.ForeignKey('taxonomy.Topic', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey('taxonomy.Country', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

class Comment(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending Moderation'
        APPROVED = 'APPROVED', 'Approved'
        FLAGGED = 'FLAGGED', 'Flagged for Review'
        REJECTED = 'REJECTED', 'Rejected'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user} on {self.article_id}"
