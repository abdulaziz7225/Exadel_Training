from rest_framework import viewsets
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.request.filters import RequestFilter
from apps.request.models import Request, RequestStatus
from apps.request.permissions import IsStaffOrReadOnly, IsStaff, IsClient, IsCompany 
from apps.request.serializers import RequestStatusSerializer, RequestSerializer, SimpleRequestStatusSerializer, SimpleRequestSerializer


# RequestStatus model
class RequestStatusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = RequestStatus.objects.all()
    serializer_class = SimpleRequestStatusSerializer
    permission_classes = [IsStaffOrReadOnly]
    

# Request model
class RequestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    # queryset = Request.objects.select_related('client', 'company', 'status', 'service').all()
    serializer_class = SimpleRequestSerializer
    permission_classes = [IsStaff | IsClient | IsCompany]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RequestFilter
    search_fields = ['name', 'service__name']
    ordering_fields = ['total_area', 'created_at']


    def get_queryset(self):
        queryset = Request.objects.select_related('client', 'company', 'status', 'service').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(Q(client=self.request.user.id) | Q(company=self.request.user.id))
        return queryset