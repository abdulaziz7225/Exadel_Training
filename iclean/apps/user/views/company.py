from rest_framework import viewsets

from apps.user.models import Company
from apps.user.permissions import IsStaff, IsCompany 
from apps.user.serializers.company import ReadCompanySerializer, CreateCompanySerializer


# Company model 
class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsStaff | IsCompany]

    def get_queryset(self):
        queryset = Company.objects.select_related('user').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(user=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CreateCompanySerializer
        return ReadCompanySerializer