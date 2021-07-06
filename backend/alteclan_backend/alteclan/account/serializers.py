from rest_framework import serializers
from django.conf import settings
from .models import Profile

User = settings.AUTH_USER_MODEL

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
