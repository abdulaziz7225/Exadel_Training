from rest_framework import serializers
from apps.user.models import Role, User, Client, Company


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'phone', 'country', 'city', 'is_staff', 'is_active']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['user', 'first_name', 'last_name', 'street', 'house_number', 'apartment']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['user', 'name']