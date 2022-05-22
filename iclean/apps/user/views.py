from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

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


    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create role"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def update(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response({"message": "You don't have permission to update role"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def destroy(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Item has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You don't have permission to delete role"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


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

    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create user"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


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

    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return Client.objects.all()
        return Client.objects.select_related('user').filter(user=self.request.user.id)

    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create client"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


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

    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return Company.objects.all()
        return Company.objects.select_related('user').filter(user=self.request.user.id)
 
    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create company"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
