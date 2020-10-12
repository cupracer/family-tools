from rest_framework import routers
from django.urls import path, include
from .viewsets import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
