
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user import views
from apps.notification.urls import router as notification_router
from apps.review.urls import router as review_router
from apps.request.urls import router as request_router
from apps.service.urls import router as service_router

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.registry.extend(notification_router.registry)
router.registry.extend(review_router.registry)
router.registry.extend(request_router.registry)
router.registry.extend(service_router.registry)


router.register(r'roles', views.RoleViewSet,basename="roles")
router.register(r'users', views.UserViewSet,basename="users")
router.register(r'clients', views.ClientViewSet,basename="clients")
router.register(r'companies', views.CompanyViewSet,basename="companies")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]