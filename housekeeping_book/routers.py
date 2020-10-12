from rest_framework import routers
from django.urls import path, include
from .viewsets import AccountHolderViewSet, CategoryViewSet, BookingViewSet, PeriodicBookingsViewSet

router = routers.DefaultRouter()

router.register('account_holders', AccountHolderViewSet)
router.register('categories', CategoryViewSet)
router.register('bookings', BookingViewSet)
router.register('periodic_bookings', PeriodicBookingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
