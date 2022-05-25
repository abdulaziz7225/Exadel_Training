from rest_framework import serializers

from apps.service.models import Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.ReadOnlyField(source='company.name')
    requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    class Meta:
        model = Service
        fields = ['url', 'id', 'name', 'type_of_service', 'cost_of_service', 'created_at', 'company', 'requests']
