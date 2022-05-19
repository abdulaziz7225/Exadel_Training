from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.service import views

urlpatterns = [
    path('', views.ServiceList.as_view(), name='service-list'),
    path('<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),
    path('<int:pk>/highlight/', views.ServiceHighlight.as_view(), name='service-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)