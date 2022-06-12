from rest_framework import serializers

from apps.notification.models import Notification


class ReadNotificationSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='email', read_only=True)
    request = serializers.SlugRelatedField(slug_field='name', read_only=True)
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'sender', 'created_at', 'request', 'company', 'slug']


class AdminCreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'sender', 'request', 'company']


class ClientCreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'request', 'company']


class CompanyCreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'request']