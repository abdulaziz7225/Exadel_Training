from rest_framework import serializers

from apps.request.models import RequestStatus, Request
from apps.service.models import Service
from apps.user.models import Client, Company


class RequestStatusSerializer(serializers.HyperlinkedModelSerializer):
    requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    class Meta:
        model = RequestStatus
        fields = ['url', 'id', 'name', 'requests']

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(slug_field='first_name', queryset=Client.objects.all())
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    status = serializers.SlugRelatedField(slug_field='name', queryset=RequestStatus.objects.all())
    service = serializers.SlugRelatedField(slug_field='name', queryset=Service.objects.all())
    notifications = serializers.HyperlinkedRelatedField(many=True, view_name='notification-detail', read_only=True)
    class Meta:
        model = Request
        fields = ['url', 'id', 'name', 'total_area', 'created_at', 'client', 'company', 'status', 'service', 'notifications']
