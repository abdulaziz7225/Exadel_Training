from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.notification import views

urlpatterns = [
    path('', views.NotificationList.as_view(), name='notification-list'),
    path('<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('<int:pk>/highlight/', views.NotificationHighlight.as_view(), name='notification-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)