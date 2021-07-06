
from rest_framework import viewsets
from django.contrib.auth import  get_user_model
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

