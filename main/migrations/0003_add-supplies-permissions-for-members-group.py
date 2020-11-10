from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations
from supplies.models import Category, Brand, Supply, SupplyItem


def make_permissions(apps,schema_editor):
    emit_post_migrate_signal(2, False, 'default')
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model('contenttypes', 'ContentType')
    member, created = Group.objects.get_or_create(name='members')

    # category

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Category),
            codename='add_category'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Category),
            codename='view_category'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Category),
            codename='delete_category'
        )
    )

    # brand

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Brand),
            codename='add_brand'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Brand),
            codename='view_brand'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Brand),
            codename='delete_brand'
        )
    )

    # supply

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Supply),
            codename='add_supply'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Supply),
            codename='view_supply'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Supply),
            codename='change_supply'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Supply),
            codename='delete_supply'
        )
    )

    # supply_item

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(SupplyItem),
            codename='add_supplyitem'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(SupplyItem),
            codename='view_supplyitem'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(SupplyItem),
            codename='change_supplyitem'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(SupplyItem),
            codename='delete_supplyitem'
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_create-members-group-with-permissions'),
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_permissions, reverse_code=lambda *args, **kwargs: True)
    ]
