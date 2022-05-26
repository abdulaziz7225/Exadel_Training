from rest_framework import serializers

from apps.user.models import Role, User, Client, Company


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    class Meta:
        model = Role
        fields = ['url', 'id', 'role', 'users']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    role = serializers.SlugRelatedField(slug_field='role', queryset=Role.objects.all())
    # role = serializers.ReadOnlyField(source='role.name')
    # clients = serializers.HyperlinkedRelatedField(many=True, view_name='client-detail', read_only=True)
    # companies = serializers.HyperlinkedRelatedField(many=True, view_name='company-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'role', 'phone', 'country', 'city', 
                        'is_staff', 'is_active'] #, 'clients', 'companies']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.id')
    user = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all())
    requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    reviews = serializers.HyperlinkedRelatedField(many=True, view_name='review-detail', read_only=True)
    class Meta:
        model = Client
        fields = ['url', 'user', 'first_name', 'last_name', 'street', 'house_number', 
        'apartment', 'requests', 'reviews']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.id')
    user = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all())
    services = serializers.HyperlinkedRelatedField(many=True, view_name='service-detail', read_only=True)
    notifications = serializers.HyperlinkedRelatedField(many=True, view_name='notification-detail', read_only=True)

    class Meta:
        model = Company
        fields = ['url', 'user', 'name', 'services', 'notifications']

