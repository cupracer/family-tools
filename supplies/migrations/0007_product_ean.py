# Generated by Django 3.1.2 on 2021-01-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0006_auto_20201215_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ean',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='EAN'),
        ),
    ]
