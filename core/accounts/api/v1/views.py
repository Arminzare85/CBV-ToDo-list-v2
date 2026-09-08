from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
     ProfileSerializer , 
     UserRegisterSerializer,
     EmailVerificationSerializer,
     )
from accounts.models import Profile
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

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

class UserVerifyView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmailVerificationSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        return Response(
            {'message': 'Verification email sent'},
            status=status.HTTP_200_OK
        )


class VerifyEmailView(APIView):

    def get(self, request, uid, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)

            if user.profile.is_verified:
                return Response(
                    {'message': 'Email already verified'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not default_token_generator.check_token(user, token):
                return Response(
                    {'message': 'Invalid or expired token'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.profile.is_verified = True
            user.profile.save(update_fields=['is_verified'])

            return Response(
                {'message': 'Email verified successfully'},
                status=status.HTTP_200_OK
            )

        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            return Response(
                {'message': 'Invalid verification link'},
                status=status.HTTP_400_BAD_REQUEST
            )