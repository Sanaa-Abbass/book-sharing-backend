from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    queryset = Book.objects.all().order_by("-created_at")

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            owner=self.request.user
        )