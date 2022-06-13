from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from apps.user.filters import UserFilter
from apps.user.models import User
from apps.user.permissions import IsStaff, IsNotStaff
from apps.user.serializers.user import ReadUserSerializer, AdminCreateUserSerializer, NonAdminCreateUserSerializer
from apps.user.serializers.register import UpdateUserSerializer


# User model 
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsStaff | IsNotStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


    # def get_serializer_context(self):
    #     return super().get_serializer_context()

    def get_queryset(self):
        queryset = User.objects.select_related('role').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset


    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateUserSerializer
        elif self.action in ["create", "destroy"]:
            if self.request.user.is_staff or self.request.user.is_anonymous:
                return AdminCreateUserSerializer
            return NonAdminCreateUserSerializer
        return ReadUserSerializer