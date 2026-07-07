from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import BorrowRequest
from .serializers import BorrowRequestSerializer

class BorrowRequestViewSet(viewsets.ModelViewSet):

    serializer_class = BorrowRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowRequest.objects.filter(
            borrower=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            borrower=self.request.user
        )
