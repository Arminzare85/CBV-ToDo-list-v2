from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User

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
        return user
    
    class Meta:
        model = User
        fields = ('username','email', 'password', 'password1')
        extra_kwargs = {
            'password': {'write_only': True},
            'password1': {'write_only': True},
        }