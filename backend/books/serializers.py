from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(
        source="owner.username"
    )

    class Meta:

        model = Book

        fields = [
            "id",
            "owner",
            "title",
            "author",
            "description",
            "image",
            "language",
            "category",
            "condition",
            "available",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "title": {
                "required": True,
                "allow_blank": False
            },
            "author": {
                "required": True,
                "allow_blank": False
            },
            "condition": {
                "required": True,
                "allow_blank": False
            }
        }