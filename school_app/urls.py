from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")


urlpatterns = [
    path("", include(router.urls)),
]