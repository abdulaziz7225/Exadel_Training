from django.urls import path
from . import views

app_name = 'notification'
# app_name = 'company'
# app_name = 'client'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='all'),
    path('<int:pk>/detail', views.NotificationDetailView.as_view(),
         name='notification_detail'),
    path('create/', views.NotificationCreateView.as_view(),
         name='notification_create'),
    path('<int:pk>/update/',
         views.NotificationUpdateView.as_view(), name='notification_update'),
    path('<int:pk>/delete/',
         views.NotificationDeleteView.as_view(), name='notification_delete'),
]
