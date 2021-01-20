from rest_framework import serializers
from .models import Category, Brand, Supply, Unit, SupplyItem, Packaging, Product


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
    num_items = serializers.IntegerField(read_only=True)
    order_value = serializers.IntegerField(read_only=True)

    class Meta:
        model = Supply
        fields = ('id', 'name', 'category', 'min_count', 'num_items', 'order_value')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    supply = SupplySerializer()
    brand = BrandSerializer()
    unit = UnitSerializer()
    packaging = PackagingSerializer()
    num_items = serializers.IntegerField(read_only=True)
    order_value = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'supply', 'name', 'brand', 'ean', 'unit', 'amount', 'bio_label', 'packaging', 'min_count', 'num_items', 'order_value')


class SupplyItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SupplyItem
        fields = ('id', 'product', 'purchase_date', 'best_before_date')
