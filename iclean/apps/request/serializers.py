from rest_framework import serializers

from apps.request.models import RequestStatus, Request


class RequestStatusSerializer(serializers.HyperlinkedModelSerializer):
    requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    class Meta:
        model = RequestStatus
        fields = ['url', 'id', 'name', 'requests']

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.ReadOnlyField(source='client.first_name')
    company = serializers.ReadOnlyField(source='company.name')
    status = serializers.ReadOnlyField(source='status.name')
    service = serializers.ReadOnlyField(source='service.name')
    notifications = serializers.HyperlinkedRelatedField(many=True, view_name='notification-detail', read_only=True)
    class Meta:
        model = Request
        fields = ['url', 'id', 'name', 'total_area', 'created_at', 'client', 'company', 'status', 'service', 'notifications']


