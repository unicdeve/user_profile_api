from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # exclude = ("is_superuser", "is_staff", "is_active", "groups", "user_permissions", "last_login")
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user', 'status_text', 'created_on', 'updated')
        extra_kwargs = {'user': {'read_only': True}}
        