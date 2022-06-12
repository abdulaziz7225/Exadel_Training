from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.service.filters import ServiceFilter
from apps.service.models import Service
from apps.service.permissions import IsStaff, IsClient, IsCompany 
from apps.service.serializers import ServiceSerializer, SimpleServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    # queryset = Service.objects.select_related('company').all()
    serializer_class = ServiceSerializer
    permission_classes = [IsStaff | IsClient | IsCompany]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ServiceFilter
    search_fields = ['name', 'type_of_service']
    ordering_fields = ['cost_of_service', 'created_at']

    def get_queryset(self):
        queryset = Service.objects.select_related('company').all()
        company = getattr(self.request.user, "companys", None)
        if company is not None:
            queryset = queryset.filter(company=company.user.id)
        return queryset