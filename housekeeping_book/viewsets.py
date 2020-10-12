from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_datatables import filters

from .serializers import AccountHolderSerializer, CategorySerializer, BookingSerializer, PeriodicBookingSerializer
from .models import AccountHolder, Category, Booking, PeriodicBooking


class AccountHolderViewSet(viewsets.ModelViewSet):
    queryset = AccountHolder.objects.all()
    serializer_class = AccountHolderSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DatatablesFilterBackend]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RecentResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class PeriodicBookingsViewSet(viewsets.ModelViewSet):
    queryset = PeriodicBooking.objects.all()
    serializer_class = PeriodicBookingSerializer
