from rest_framework import serializers
from .models import BorrowRequest


class BorrowRequestSerializer(serializers.ModelSerializer):
    borrower = serializers.ReadOnlyField(
        source="borrower.username"
    )

    class Meta:
        model = BorrowRequest
        fields = [
            "id",
            "book",
            "borrower",
            "status",
            "request_date",
            "due_date",
        ]

    def validate_book(self, book):

        user = self.context["request"].user

        # Cannot borrow your own book
        if book.owner == user:
            raise serializers.ValidationError(
                "You cannot borrow your own book."
            )

        # Book must be available
        if not book.available:
            raise serializers.ValidationError(
                "This book is currently unavailable."
            )

        # Prevent duplicate pending requests
        exists = BorrowRequest.objects.filter(
            borrower=user,
            book=book,
            status=BorrowRequest.PENDING
        ).exists()

        if exists:
            raise serializers.ValidationError(
                "You already have a pending request for this book."
            )

        return book