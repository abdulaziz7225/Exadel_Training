from rest_framework import viewsets

from apps.service.models import Service
from apps.service.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

