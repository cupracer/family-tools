# Generated by Django 3.1.2 on 2020-11-11 07:21

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('housekeeping_book', '0003_auto_20201014_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountholder',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': [django.db.models.functions.text.Lower('name')], 'verbose_name_plural': 'categories'},
        ),
    ]