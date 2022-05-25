from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.request import views


urlpatterns = [
     path('', views.RequestList.as_view(), name='request-list'),
     path('<int:pk>/', views.RequestDetail.as_view(), name='request-detail'),

     # path('status/', views.RequestStatusList.as_view(), name='request-status-list'),
     # path('status/<int:pk>/', views.RequestStatusDetail.as_view(), name='request-status-detail'),
]    

urlpatterns = format_suffix_patterns(urlpatterns)

