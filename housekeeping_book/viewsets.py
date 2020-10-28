from datetime import datetime

from django.db.models import Count, Case, When, Value, BooleanField
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_datatables import filters

from .serializers import AccountHolderSerializer, CategorySerializer, BookingSerializer, PeriodicBookingSerializer
from .models import AccountHolder, Category, Booking, PeriodicBooking


class AccountHolderViewSet(viewsets.ModelViewSet):
    queryset = AccountHolder.objects.all().annotate(
        num_bookings=Count('booking', distinct=True) + Count('periodicbooking', distinct=True))
    serializer_class = AccountHolderSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().annotate(
        num_bookings=Count('booking', distinct=True) + Count('periodicbooking', distinct=True))
    serializer_class = CategorySerializer
    filter_backends = [filters.DatatablesFilterBackend]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RecentResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class PeriodicBookingsViewSet(viewsets.ModelViewSet):
    queryset = PeriodicBooking.objects.all().annotate(
        is_active=Case(
            When(end_date__lt=datetime.now(),
                 then=Value(False, output_field=BooleanField())),
            default=Value(True)
        ),
    )
    serializer_class = PeriodicBookingSerializer
