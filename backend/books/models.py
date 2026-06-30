from django.db import models
from django.conf import settings

from users.models import User



class Book(models.Model):

    class Condition(models.TextChoices):
        NEW = "NEW", "New"
        LIKE_NEW = "LIKE_NEW", "Like New"
        GOOD = "GOOD", "Good"
        FAIR = "FAIR", "Fair"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )

    title = models.CharField(
        max_length=255
    )

    author = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="books/",
        null=True,
        blank=True
    )

    language = models.CharField(
        max_length=50,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.GOOD
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books"
    )

    title = models.CharField(max_length=255)

    author = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="books/",
        blank=True,
        null=True
    )

    language = models.CharField(
        max_length=50,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    condition = models.CharField(
        max_length=50
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )

    title = models.CharField(max_length=255)

    author = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='books/',
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title