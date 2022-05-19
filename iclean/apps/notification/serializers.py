from rest_framework import serializers


from apps.notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'name', 'details', 'viewed_by_company', 'created_at', 'request', 'company']