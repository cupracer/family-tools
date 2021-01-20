from django.db import models
from django.db.models.functions import Lower

from main.validators import validate_item_name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=200, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = [Lower('name')]


class Brand(models.Model):
    name = models.CharField(unique=True, max_length=200, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Lower('name')]


class Unit(models.Model):
    name = models.CharField(unique=True, max_length=3, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Lower('name')]


class Packaging(models.Model):
    name = models.CharField(unique=True, max_length=100, validators=[validate_item_name])

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Lower('name')]


class Supply(models.Model):
    name = models.CharField(null=True, blank=True, max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=False)
    min_count = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'category')


class Product(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, null=False, blank=False)
    name = models.CharField(null=True, blank=True, max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)
    ean = models.CharField('EAN', null=True, blank=True, max_length=13)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False, blank=False)
    amount = models.IntegerField()
    bio_label = models.BooleanField('Bio', default=False)
    packaging = models.ForeignKey(Packaging, on_delete=models.PROTECT, null=True, blank=True)
    min_count = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        custom = self.supply.name
        if self.name:
            custom += ' - ' + self.name
        if self.brand:
            custom += ' - ' + self.brand.name
        custom += ' - ' + str(self.amount)
        custom += ' ' + self.unit.name
        return custom

    class Meta:
        unique_together = ('supply', 'name', 'brand', 'unit', 'amount', 'packaging')


class SupplyItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=False)
    purchase_date = models.DateField('purchase date', null=True, blank=True)
    best_before_date = models.DateField('best-before date', null=True, blank=True)
    checkout_date = models.DateField('checkout date', null=True, blank=True)
