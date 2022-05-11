from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("register/", views.say_hello),
    path("login/", views.say_hello),

]
