from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = Profile
        fields = ('full_name', 'bio', 'avatar', 'is_verified', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        if data['password'] != data['password1']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    def create(self, validated_data):
        validated_data.pop('password1')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user
    
    class Meta:
        model = User
        fields = ('username','email', 'password', 'password1')
        extra_kwargs = {
            'password': {'write_only': True},
            'password1': {'write_only': True},
        }


class EmailVerificationSerializer(serializers.Serializer):
    def validate(self, attrs):
        user = self.context['request'].user
        if user.profile.is_verified:
            raise serializers.ValidationError(
                'Email already verified'
            )
        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )
        token = default_token_generator.make_token(user)
        verification_url = self.context['request'].build_absolute_uri(
            reverse(
                'accounts:confirm-email',
                kwargs={
                    'uid': uid,
                    'token': token
                }
            )
        )
        print("USER:", user)
        print("EMAIL:", user.email)
        send_mail(
            'Verify your email',
            f'Click this link to verify your email:\n\n{verification_url}',
            None,
            [user.email],
        )
        
        return attrs