# from django.urls import path, include
# from apps.user.register.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
# from rest_framework.routers import SimpleRouter


# # router = SimpleRouter()


# urlpatterns = [
#     # path('', include(router.urls)),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('register/', RegisterView.as_view(), name='auth_register'),
#     path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
#     path('update-profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
#     path('logout/', LogoutView.as_view(), name='auth_logout'),
#     path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
# ]