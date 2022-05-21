from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.request import views


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'requests', views.RequestViewSet,basename="requests")
# router.register(r'request-statuses', views.RequestStatusViewSet,basename="request-statuses")

# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

