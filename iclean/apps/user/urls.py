from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user import views
from apps.notification import views as notification_view
from apps.request import views as request_view
from apps.review import views as review_view
from apps.service import views as service_view


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'notifications', notification_view.NotificationViewSet,basename="notifications")
router.register(r'requests', request_view.RequestViewSet,basename="requests")
router.register(r'request-statuses', request_view.RequestStatusViewSet,basename="request-statuses")
router.register(r'reviews', review_view.ReviewViewSet, basename="reviews")
router.register(r'services', service_view.ServiceViewSet,basename="services")

router.register(r'roles', views.RoleViewSet, basename="roles")
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'clients', views.ClientViewSet, basename="clients")
router.register(r'companies', views.CompanyViewSet, basename="companies")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
