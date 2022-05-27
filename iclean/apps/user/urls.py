from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user import views
from apps.notification.views import NotificationViewSet
from apps.request.views import RequestViewSet, RequestStatusViewSet
from apps.review.views import ReviewViewSet
from apps.service.views import ServiceViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'notifications', NotificationViewSet,basename="notifications")
router.register(r'requests', RequestViewSet,basename="requests")
router.register(r'request-statuses', RequestStatusViewSet,basename="requeststatuses")
router.register(r'reviews', ReviewViewSet, basename="reviews")
router.register(r'services', ServiceViewSet,basename="services")

router.register(r'roles', views.RoleViewSet, basename="roles")
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'clients', views.ClientViewSet, basename="clients")
router.register(r'companies', views.CompanyViewSet, basename="companies")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
