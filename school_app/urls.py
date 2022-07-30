from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")
router.register("student", StudentViewSet, basename="student")



urlpatterns = [
    path("", include(router.urls)),
    path('student/<int:pk>/update/', StudentViewSet.as_view({"post": "partial_update"}), name="student_update"),
]