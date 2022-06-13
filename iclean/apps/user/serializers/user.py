from rest_framework import serializers

from apps.user.models import Role, User


# User model
class ReadUserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(slug_field='role', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'role', 'phone', 'country', 'city', 'is_staff', 'is_active']


class AdminCreateUserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(slug_field='role', queryset=Role.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'role', 'phone', 'country', 'city', 'is_staff', 'is_active']


class NonAdminCreateUserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(slug_field='role', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'role', 'phone', 'country', 'city', 'is_staff', 'is_active']
        read_only_fields = ['email', 'is_staff', 'is_active']
