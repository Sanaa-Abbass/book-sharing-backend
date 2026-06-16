from django.contrib.auth.models import AbstractUser
from django.db import models


class InvitationCode(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.code


class User(AbstractUser):

    profile_image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True
    )

    building_name = models.CharField(
        max_length=255,
        blank=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    rating = models.FloatField(
        default=0
    )

    invitation_code = models.ForeignKey(
        InvitationCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )