from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from housekeeping_book.models import AccountHolder, Category, Booking, PeriodicBooking


class AccountHolderAdmin(GuardedModelAdmin):
    pass


class CategoryAdmin(GuardedModelAdmin):
    pass


class BookingAdmin(GuardedModelAdmin):
    pass


class PeriodicBookingAdmin(GuardedModelAdmin):
    pass


admin.site.register(AccountHolder, AccountHolderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(PeriodicBooking, PeriodicBookingAdmin)
