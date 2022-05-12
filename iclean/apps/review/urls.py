from django.urls import path
from . import views

app_name = 'review'
# app_name = 'company'
# app_name = 'client'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='all'),
    path('<int:pk>/detail', views.ReviewDetailView.as_view(),
         name='review_detail'),
    path('create/', views.ReviewCreateView.as_view(),
         name='review_create'),
    path('<int:pk>/update/',
         views.ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/',
         views.ReviewDeleteView.as_view(), name='review_delete'),
]
