from rest_framework import serializers
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = Profile
        fields = ('full_name', 'bio', 'avatar', 'is_verified', 'email')