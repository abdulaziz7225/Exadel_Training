from rest_framework import serializers

from apps.user.models import Company


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