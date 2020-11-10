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


class Supply(models.Model):
    name = models.CharField(null=True, blank=True, max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False, blank=False)
    amount = models.IntegerField()

    def __str__(self):
        custom = self.name
        if self.brand:
            custom += ' - ' + self.brand.name
        custom += ' - ' + str(self.amount)
        custom += ' ' + self.unit.name
        return custom

    class Meta:
        unique_together = ('name', 'category', 'brand', 'unit', 'amount')


class SupplyItem(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, null=False, blank=False)
    purchase_date = models.DateField('purchase date', null=True, blank=True)
    best_before_date = models.DateField('best-before date', null=True, blank=True)
