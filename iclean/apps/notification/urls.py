from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.notification import views


urlpatterns = format_suffix_patterns([
    path('', views.NotificationList.as_view(), name='notification-list'),
    path('<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
])