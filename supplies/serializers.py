from rest_framework import serializers
from .models import Category, Brand, Supply, Unit, SupplyItem


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name')


class SupplySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    unit = UnitSerializer()

    class Meta:
        model = Supply
        fields = ('id', 'name', 'category', 'brand', 'unit', 'amount')


class SupplyItemSerializer(serializers.HyperlinkedModelSerializer):
    supply = SupplySerializer()

    class Meta:
        model = SupplyItem
        fields = ('id', 'supply', 'purchase_date', 'best_before_date')
