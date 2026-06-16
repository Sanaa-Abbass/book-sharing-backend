from django.db import models
from django.conf import settings
from books.models import Book

class BorrowRequest(models.Model):

    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    RETURNED = 'returned'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (RETURNED, 'Returned'),
    ]

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    request_date = models.DateTimeField(
        auto_now_add=True
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )