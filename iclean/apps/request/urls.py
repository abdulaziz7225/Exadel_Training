from django.urls import path
from . import views

app_name = 'request'


urlpatterns = [
    path('', views.RequestListView.as_view(), name='all'),
    path('<int:pk>/detail', views.RequestDetailView.as_view(),
         name='request_detail'),
    path('create/', views.RequestCreateView.as_view(),
         name='request_create'),
    path('<int:pk>/update/',
         views.RequestUpdateView.as_view(), name='request_update'),
    path('<int:pk>/delete/',
         views.RequestDeleteView.as_view(), name='request_delete'),
]
