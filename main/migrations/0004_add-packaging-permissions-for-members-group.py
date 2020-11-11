from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations
from supplies.models import Packaging


def make_permissions(apps,schema_editor):
    emit_post_migrate_signal(2, False, 'default')
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model('contenttypes', 'ContentType')
    member, created = Group.objects.get_or_create(name='members')

    # packaging

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Packaging),
            codename='add_packaging'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Packaging),
            codename='view_packaging'
        )
    )

    member.permissions.add(
        Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Packaging),
            codename='delete_packaging'
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_add-supplies-permissions-for-members-group'),
        ('supplies', '0002_auto_20201111_0721'),
    ]

    operations = [
        migrations.RunPython(make_permissions, reverse_code=lambda *args, **kwargs: True)
    ]
