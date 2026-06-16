from django.db import models
from django.conf import settings

class Book(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )

    title = models.CharField(max_length=255)

    author = models.CharField(max_length=255)

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='books/',
        blank=True,
        null=True
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )