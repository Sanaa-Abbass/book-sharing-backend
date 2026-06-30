from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    owner_username = serializers.CharField(
        source='owner.username',
        read_only=True
    )

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = fields = [
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