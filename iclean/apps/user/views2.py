# from requests import Request, Response
# from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action

# from apps.user.filters import UserFilter
# from apps.user.models import Role, User, Client, Company
# from apps.user.permissions import IsStaffOrReadOnly, IsStaff, IsNotStaff, IsClient, IsCompany 
# from apps.user.serializers import AdminRoleSerializer, NonAdminRoleSerializer, ReadUserSerializer, AdminCreateUserSerializer, \
#             NonAdminCreateUserSerializer, ReadClientSerializer, CreateClientSerializer, ReadCompanySerializer, CreateCompanySerializer


# # Role model
# class RoleViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides 'list', 'create', 'retrieve',
#     'update' and 'destroy' actions.
#     """
#     queryset = Role.objects.all()
#     # serializer_class = NonAdminRoleSerializer
#     permission_classes = [IsStaffOrReadOnly]

#     def get_serializer_class(self):
#         if self.request.user.is_staff:
#             return AdminRoleSerializer
#         return NonAdminRoleSerializer


# # User model 
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides 'list', 'create', 'retrieve',
#     'update' and 'destroy' actions.
#     """
#     queryset = User.objects.select_related('role').all()
#     serializer_class = ReadUserSerializer
#     permission_classes = [IsStaff | IsNotStaff]
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = UserFilter


#     # @action(detail=False, methods=['GET', 'PUT'])
#     # def me(self, request):
#     #     # serializer_context = {
#     #     #     'request': Request(request),
#     #     # }
#     #     # (user, created) = User.objects.get_or_create(id=request.user.id)
#     #     if request.method == 'GET':
#     #         # serializer = NonAdminCreateUserSerializer(user)
#     #         # return Response(serializer.data)
#     #         return Response('OK')
#     #     elif request.method == "PUT":
#     #         # serializer = NonAdminCreateUserSerializer(user, data=request.data)
#     #         # serializer.is_valid(raise_exception=True)
#     #         # serializer.save()
#     #         # return Response(serializer.data)
#     #         return Response('OK2')


#     def get_serializer_context(self):
#         return super().get_serializer_context()

#     def get_queryset(self):
#         queryset = User.objects.select_related('role').all()
#         is_staff = getattr(self.request.user, "is_staff", None)
#         if not is_staff:
#             queryset = queryset.filter(id=self.request.user.id)
#         return queryset


#     def get_serializer_class(self):
#         if self.action in ["create", "update", "partial_update", "destroy"]:
#             if self.request.user.is_staff or self.request.user.is_anonymous:
#                 return AdminCreateUserSerializer
#             return NonAdminCreateUserSerializer
#         return ReadUserSerializer
    

#     # def perform_create(self, serializer):
#     #     serializer.save(client=self.request.user.clients)

#     # def perform_create(self, serializer):
#     #     if self.request.user.role.role == 'client':
#     #         serializer.save(sender=self.request.user)
#     #     elif self.request.user.role.role == 'company':
#     #         serializer.save(sender=self.request.user, company=self.request.user.companys)

# # Client model
# class ClientViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides 'list', 'create', 'retrieve',
#     'update' and 'destroy' actions.
#     """
#     queryset = Client.objects.select_related('user').all()
#     # serializer_class = ReadClientSerializer
#     permission_classes = [IsStaff | IsClient]

#     # @action(detail=False)
#     # def me(self, request):
#     #     return Response('ok')

#     def get_queryset(self):
#         queryset = Client.objects.select_related('user').all()
#         is_staff = getattr(self.request.user, "is_staff", None)
#         if not is_staff:
#             queryset = queryset.filter(user=self.request.user.id)
#         return queryset


#     def get_serializer_class(self):
#         if self.action in ["create", "update", "partial_update", "destroy"]:
#             return CreateClientSerializer
#         return ReadClientSerializer


# # Company model 
# class CompanyViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides 'list', 'create', 'retrieve',
#     'update' and 'destroy' actions.
#     """
#     queryset = Company.objects.select_related('user').all()
#     # serializer_class = ReadCompanySerializer
#     permission_classes = [IsStaff | IsCompany]

#     def get_queryset(self):
#         queryset = Company.objects.select_related('user').all()
#         is_staff = getattr(self.request.user, "is_staff", None)
#         if not is_staff:
#             queryset = queryset.filter(user=self.request.user.id)
#         return queryset

#     def get_serializer_class(self):
#         if self.action in ["create", "update", "partial_update", "destroy"]:
#             return CreateCompanySerializer
#         return ReadCompanySerializer