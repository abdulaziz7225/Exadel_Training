from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from apps.user.models import Role, User, Client, Company
from apps.user.serializers import RoleSerializer, UserSerializer, ClientSerializer, CompanySerializer


"""
root api
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'notification': reverse('notification-list', request=request, format=format),
        'review': reverse('review-list', request=request, format=format),
        'status': reverse('requeststatus-list', request=request, format=format),
        'request': reverse('request-list', request=request, format=format),
        'service': reverse('service-list', request=request, format=format),
        'role': reverse('role-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format),
        'client': reverse('client-list', request=request, format=format),
        'company': reverse('company-list', request=request, format=format),
    })



"""
Role model
""" 
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


"""
User model 
"""
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
Client model
"""  
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


"""
Company model 
"""
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

