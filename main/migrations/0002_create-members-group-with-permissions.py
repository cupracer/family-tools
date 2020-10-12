from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations
from housekeeping_book.models import AccountHolder, Category, Booking, PeriodicBooking


def make_permissions(apps,schema_editor):
    emit_post_migrate_signal(2, False, 'default')
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model('contenttypes', 'ContentType')
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

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('housekeeping_book', '0002_auto_20201012_0537'),
    ]

    operations = [
        migrations.RunPython(make_permissions, reverse_code=lambda *args, **kwargs: True)
    ]
