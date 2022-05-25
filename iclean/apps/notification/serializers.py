from rest_framework import serializers

from apps.notification.models import Notification


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    request = serializers.ReadOnlyField(source='request.name')
    company = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'viewed_by_company', 'created_at', 'request', 'company']
