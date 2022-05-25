from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.user import views
from apps.request import views as request_views


urlpatterns = format_suffix_patterns([
     path('', views.api_root),

     path('request-statuses/', request_views.RequestStatusList.as_view(), name='request-status-list'),
     path('request-statuses/<int:pk>/', request_views.RequestStatusDetail.as_view(), name='request-status-detail'),

     path('users/', views.UserList.as_view(), name='user-list'),
     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

     path('roles/', views.RoleList.as_view(), name='role-list'),
     path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),

     path('clients/', views.ClientList.as_view(), name='client-list'),
     path('clients/<int:pk>/', views.ClientDetail.as_view(), name='client-detail'),

     path('companies/', views.CompanyList.as_view(), name='company-list'),
     path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),

])
