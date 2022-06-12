from django_filters.rest_framework import FilterSet, BooleanFilter

from apps.notification.models import Notification


class NotificationFilter(FilterSet):
    viewed_by_company = BooleanFilter()
    class Meta:
        model = Notification
        fields = {
            'name': ['icontains'],
            # 'viewed_by_company': ['exact'],
            'request': ['exact'],
            'company': ['exact'],
        }