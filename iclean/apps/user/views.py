from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from apps.user.filters import UserFilter
from apps.user.models import Role, User, Client, Company
from apps.user.permissions import IsStaffOrReadOnly, IsStaff, IsNotStaff, IsClient, IsCompany 
from apps.user.serializers import RoleSerializer, UserSerializer, ClientSerializer, CompanySerializer
from apps.user.serializers import SimpleRoleSerializer, SimpleUserSerializer


# Role model
class RoleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Role.objects.all()
    serializer_class = SimpleRoleSerializer
    permission_classes = [IsStaffOrReadOnly]


# User model 
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = User.objects.select_related('role').all()
    serializer_class = SimpleUserSerializer
    permission_classes = [IsStaff | IsNotStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    # @action(detail=False, methods=['GET', 'PUT'])
    # def me(self, request):
    #     (user, created) = User.objects.get_or_create(id=request.user.id)
    #     if request.method == 'GET':
    #         serializer = SimpleUserSerializer(user)
    #         return Response(serializer.data)
    #     elif request.method == "PUT":
    #         serializer = SimpleUserSerializer(user, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

    # def get_serializer_context(self):
    #     return super().get_serializer_context()

    def get_queryset(self):
        queryset = User.objects.select_related('role').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset


# Client model
class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Client.objects.select_related('user').all()
    serializer_class = ClientSerializer
    permission_classes = [IsStaff | IsClient]

    # @action(detail=False)
    # def me(self, request):
    #     return Response('ok')

    def get_queryset(self):
        queryset = Client.objects.select_related('user').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(user=self.request.user.id)
        return queryset


# Company model 
class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Company.objects.select_related('user').all()
    serializer_class = CompanySerializer
    permission_classes = [IsStaff | IsCompany]

    def get_queryset(self):
        queryset = Company.objects.select_related('user').all()
        is_staff = getattr(self.request.user, "is_staff", None)
        if not is_staff:
            queryset = queryset.filter(user=self.request.user.id)
        return queryset
