from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [
    path('', views.UserListView.as_view(), name='all'),
    path('user/<int:pk>/detail', views.UserDetailView.as_view(), name='user_detail'),
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/',
         views.UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/',
         views.UserDeleteView.as_view(), name='user_delete'),

]
