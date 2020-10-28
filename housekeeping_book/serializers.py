from rest_framework import serializers

from main.models import User
from .models import AccountHolder, Category, Booking, PeriodicBooking


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')


class AccountHolderSerializer(serializers.HyperlinkedModelSerializer):
    num_bookings = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccountHolder
        fields = ('id', 'name', 'num_bookings')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    num_bookings = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'num_bookings')


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    account_holder = AccountHolderSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'url', 'user', 'booking_date', 'category', 'account_holder', 'description', 'amount')


class PeriodicBookingSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    account_holder = AccountHolderSerializer()
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = PeriodicBooking
        fields = ('id', 'url', 'user', 'category', 'account_holder', 'description', 'amount',
                  'start_date', 'end_date', 'interval', 'booking_day_of_month', 'identifier', 'is_active')
