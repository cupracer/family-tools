from django.db import models
from datetime import datetime

from guardian.models import UserObjectPermissionBase, GroupObjectPermissionBase

from main.models import User
from main.validators import validate_item_name


class AccountHolder(models.Model):
    name = models.CharField(unique=True, max_length=200, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(unique=True, max_length=200, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']


class BaseBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=False)
    account_holder = models.ForeignKey(AccountHolder, on_delete=models.PROTECT, null=True, blank=False)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.CharField(unique=False, null=True, blank=True, max_length=500)
    last_update = models.DateTimeField('last update', null=False, blank=False, default=datetime.now)

    class Meta:
        abstract = True


class Booking(BaseBooking):
    parent_identifier = models.CharField(unique=True, null=True, blank=True, max_length=32)
    booking_date = models.DateField('booking date', null=False, blank=False)

    def __str__(self):
        return str(self.booking_date.year) + "-" + str(self.booking_date.month) + "-" + str(
            self.booking_date.day) + " : " + str(self.account_holder) + " : " + str(self.amount)


class BookingUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(Booking, on_delete=models.CASCADE)


class BookingGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(Booking, on_delete=models.CASCADE)


class PeriodicBooking(BaseBooking):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    interval = models.IntegerField(default=1, null=False, blank=False)
    identifier = models.CharField(unique=True, null=True, blank=False, max_length=32)
    booking_day_of_month = models.IntegerField('DOM', default=1, null=False, blank=False)


class PeriodicBookingUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(PeriodicBooking, on_delete=models.CASCADE)


class PeriodicBookingGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(PeriodicBooking, on_delete=models.CASCADE)
