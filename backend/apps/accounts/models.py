import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        VISITOR = 'VISITOR', 'Visitor'
        READER = 'READER', 'Registered Reader'
        CONTRIBUTOR = 'CONTRIBUTOR', 'Contributor / Reporter'
        EDITOR = 'EDITOR', 'Editor'
        SENIOR_EDITOR = 'SENIOR_EDITOR', 'Senior / Managing Editor'
        ADMIN = 'ADMIN', 'Publisher / Administrator'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.READER,
        db_index=True
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    two_factor_enabled = models.BooleanField(default=False)
    newsletter_subscribed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def is_editorial_staff(self):
        return self.role in [self.Role.EDITOR, self.Role.SENIOR_EDITOR, self.Role.ADMIN]

    def is_contributor(self):
        return self.role in [self.Role.CONTRIBUTOR, self.Role.EDITOR, self.Role.SENIOR_EDITOR, self.Role.ADMIN]

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
