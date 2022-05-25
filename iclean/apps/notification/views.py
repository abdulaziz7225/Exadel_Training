from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer


class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
