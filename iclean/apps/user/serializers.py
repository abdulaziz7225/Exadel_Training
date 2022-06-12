from rest_framework import serializers

from apps.user.models import Role, User, Client, Company


# Role model
class AdminRoleSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    class Meta:
        model = Role
        fields = ['url', 'id', 'role', 'users']


class NonAdminRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['url', 'id', 'role']


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


# Client model
class ReadClientSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    # requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    # reviews = serializers.HyperlinkedRelatedField(many=True, view_name='review-detail', read_only=True)
    class Meta:
        model = Client
        fields = ['url', 'user', 'first_name', 'last_name', 'street', 'house_number', 
        'apartment', 'requests', 'reviews']


class CreateClientSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    class Meta:
        model = Client
        fields = ['url', 'user', 'first_name', 'last_name', 'street', 'house_number', 'apartment']


# Company model
class ReadCompanySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    # services = serializers.HyperlinkedRelatedField(many=True, view_name='service-detail', read_only=True)
    # notifications = serializers.HyperlinkedRelatedField(many=True, view_name='notification-detail', read_only=True)

    class Meta:
        model = Company
        fields = ['url', 'user', 'name', 'services', 'notifications']


class CreateCompanySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    class Meta:
        model = Company
        fields = ['url', 'user', 'name' ]