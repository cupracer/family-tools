from rest_framework import routers
from django.urls import path, include
from .viewsets import UserViewSet

router = routers.DefaultRouter()

main_router = routers.DefaultRouter()
main_router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('main/', include(main_router.urls)),
    path('housekeeping_book/', include('housekeeping_book.routers')),
    path('supplies/', include('supplies.routers')),
]
