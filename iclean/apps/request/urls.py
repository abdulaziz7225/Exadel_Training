from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.request import views


urlpatterns = format_suffix_patterns([
     path('', views.RequestList.as_view(), name='request-list'),
     path('<int:pk>/', views.RequestDetail.as_view(), name='request-detail'),
])

