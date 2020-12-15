# Generated by Django 3.1.2 on 2020-12-15 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0003_supplyitem_checkout_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('bio_label', models.BooleanField(default=False, verbose_name='Bio')),
                ('min_count', models.IntegerField(blank=True, default=None, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplies.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='supplies.category')),
                ('packaging', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='supplies.packaging')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplies.supply')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplies.unit')),
            ],
            options={
                'unique_together': {('supply', 'category', 'brand', 'unit', 'amount', 'packaging')},
            },
        ),
        migrations.AddField(
            model_name='supplyitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='supplies.product'),
        ),
    ]
