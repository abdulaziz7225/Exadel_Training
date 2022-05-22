from rest_framework import serializers

from apps.request.models import Request_status, Request
from apps.service.models import Service
from apps.user.models import Client, Company


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request_status
        fields = ['id', 'name']


class RequestSerializer(serializers.ModelSerializer):
    # client = serializers.SlugRelatedField(slug_field='full_name', queryset=Client.objects.all())
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    status = serializers.SlugRelatedField(slug_field='name', queryset=Request_status.objects.all())
    service = serializers.SlugRelatedField(slug_field='name', queryset=Service.objects.all())
    class Meta:
        model = Request
        fields = ['id', 'name', 'total_area', 'created_at', 'client', 'company', 'status', 'service']

