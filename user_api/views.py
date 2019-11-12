from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
