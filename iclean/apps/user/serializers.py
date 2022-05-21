from rest_framework import serializers

from apps.user.models import Role, User, Client, Company


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(slug_field='role', queryset=Role.objects.all())
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'phone',
                  'country', 'city', 'is_staff', 'is_active']


class ClientSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Client
        fields = ['user', 'first_name', 'last_name',
                  'street', 'house_number', 'apartment']


class CompanySerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Company
        fields = ['user', 'name']
