from rest_framework import viewsets

from apps.user.models import Company
from apps.user.permissions import IsStaff, IsCompany 
from apps.user.serializers.company import ReadCompanySerializer, UpdateCompanySerializer, AdminCreateCompanySerializer, NonAdminCreateCompanySerializer


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
        if self.action in ["update", "partial_update"]:
            return UpdateCompanySerializer
        elif self.action in ["create", "destroy"]:
            if self.request.user.is_staff:
                return AdminCreateCompanySerializer
            return NonAdminCreateCompanySerializer
        return ReadCompanySerializer


    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(user=self.request.user)
        serializer.save()