
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.user import views

urlpatterns = [
     path('', views.api_root),

     path('users/', views.UserList.as_view(), name='user-list'),
     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

     path('roles/', views.RoleList.as_view(), name='role-list'),
     path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),

     path('clients/', views.ClientList.as_view(), name='client-list'),
     path('clients/<int:pk>/', views.ClientDetail.as_view(), name='client-detail'),

     path('companies/', views.CompanyList.as_view(), name='company-list'),
     path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)