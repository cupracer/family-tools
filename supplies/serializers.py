from rest_framework import serializers
from .models import Category, Brand, Supply, Unit, SupplyItem, Packaging


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


class PackagingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Packaging
        fields = ('id', 'name')


class SupplySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    unit = UnitSerializer()
    packaging = PackagingSerializer()

    class Meta:
        model = Supply
        fields = ('id', 'name', 'category', 'brand', 'unit', 'amount', 'bio_label', 'packaging', 'min_count')


class SupplyItemSerializer(serializers.HyperlinkedModelSerializer):
    supply = SupplySerializer()

    class Meta:
        model = SupplyItem
        fields = ('id', 'supply', 'purchase_date', 'best_before_date')
