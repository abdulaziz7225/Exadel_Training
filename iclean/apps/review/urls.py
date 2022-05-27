from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.review import views


urlpatterns = format_suffix_patterns([
    path('', views.ReviewList.as_view(), name='review-list', ),
    path('<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
])