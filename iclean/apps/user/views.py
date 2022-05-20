from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.user.models import Role, User, Client, Company
from apps.user.serializers import RoleSerializer, UserSerializer, ClientSerializer, CompanySerializer



"""
Role model
"""
class RoleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


"""
User model 
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
Client model
"""
class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


"""
Company model 
"""
class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

