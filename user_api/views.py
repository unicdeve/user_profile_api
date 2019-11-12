from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import models
from .serializers import UserProfileSerializer
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
