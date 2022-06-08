from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.notification.urls import router as notification_router
from apps.request.urls import router as request_router
from apps.review.urls import router as review_router
from apps.service.urls import router as service_router

from apps.user import views


router = DefaultRouter()
router.registry.extend(notification_router.registry)
router.registry.extend(request_router.registry)
router.registry.extend(review_router.registry)
router.registry.extend(service_router.registry)

router.register(r'roles', views.RoleViewSet, basename="role")
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'clients', views.ClientViewSet, basename="client")
router.register(r'companys', views.CompanyViewSet, basename="company")


urlpatterns = [
    path('', include(router.urls)),
]
