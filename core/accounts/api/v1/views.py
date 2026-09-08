from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
     ProfileSerializer , 
     UserRegisterSerializer
     )
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Profile,user=self.request.user)



class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)