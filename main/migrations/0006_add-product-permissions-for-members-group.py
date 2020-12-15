from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations
from supplies.models import Packaging, Product


def make_permissions(apps,schema_editor):
    emit_post_migrate_signal(2, False, 'default')
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model('contenttypes', 'ContentType')
    member, created = Group.objects.get_or_create(name='members')

    # packaging

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Product),
            codename='add_product'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Product),
            codename='view_product'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Product),
            codename='change_product'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Product),
            codename='delete_product'
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0005_user_todoist_api_key'),
        ('supplies', '0005_auto_20201215_0931'),
    ]

    operations = [
        migrations.RunPython(make_permissions, reverse_code=lambda *args, **kwargs: True)
    ]
