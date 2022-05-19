from rest_framework import serializers
from apps.request.models import Request


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'name']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'name', 'total_area', 'created_at', 'client', 'company', 'status', 'service']

