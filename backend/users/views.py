from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer



class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "building_name": request.user.building_name,
            "is_verified": request.user.is_verified,
        })
