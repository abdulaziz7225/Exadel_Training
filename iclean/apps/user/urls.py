from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user import views
from apps.notification.views import NotificationViewSet
from apps.request.views import RequestViewSet, RequestStatusViewSet
from apps.review.views import ReviewViewSet
from apps.service.views import ServiceViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'notifications', NotificationViewSet,basename="notification")
router.register(r'requests', RequestViewSet,basename="request")
router.register(r'requeststatuses', RequestStatusViewSet,basename="requeststatus")
router.register(r'reviews', ReviewViewSet, basename="review")
router.register(r'services', ServiceViewSet,basename="service")

router.register(r'roles', views.RoleViewSet, basename="role")
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'clients', views.ClientViewSet, basename="client")
router.register(r'companys', views.CompanyViewSet, basename="company")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
