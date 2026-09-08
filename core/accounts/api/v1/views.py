from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import  ProfileSerializer
from accounts.models import Profile
from django.shortcuts import get_object_or_404

# Create your views here.

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Profile,user=self.request.user)