# Generated by Django 3.1.2 on 2020-11-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_add-packaging-permissions-for-members-group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='todoist_api_key',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
