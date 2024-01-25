from django.db import transaction
from rest_framework import serializers
from user.models import User
from userProfile.models import Profile
from userProfile.serializers import ProfileSerializer
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'location', 'birth_date', 'is_private', 'profile']

class UserMeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'location', 'birth_date', 'is_private', 'profile']
        extra_kwargs = {
            'username': {'read_only': True}
        }
    @transaction.atomic
    def update(self, instance, validated_data):
        profile = Profile.objects.filter(user=instance)

        profile_validated_data = validated_data.pop('profile')
        user = super().update(instance, validated_data)
        profile.update(**profile_validated_data)
        return user

