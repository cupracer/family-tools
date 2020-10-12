from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from housekeeping_book.models import AccountHolder, Category, Booking, PeriodicBooking


def populate_models(sender, **kwargs):
    member, created = Group.objects.get_or_create(name='members')

    # account_holder

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(AccountHolder),
            codename='add_accountholder'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(AccountHolder),
            codename='view_accountholder'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(AccountHolder),
            codename='delete_accountholder'
        )
    )

    # category

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Category),
            codename='view_category'
        )
    )

    # booking

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Booking),
            codename='view_booking'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Booking),
            codename='add_booking'
        )
    )

    # periodic_booking

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(PeriodicBooking),
            codename='view_periodicbooking'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(PeriodicBooking),
            codename='add_periodicbooking'
        )
    )
