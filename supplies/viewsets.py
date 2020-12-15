from django.db.models import Count, Case, When, Value, IntegerField, F
from rest_framework import viewsets
from rest_framework_datatables import filters
from django.db.models import Q

from .serializers import CategorySerializer, BrandSerializer, SupplySerializer, UnitSerializer, SupplyItemSerializer, \
    PackagingSerializer, ProductSerializer
from .models import Category, Brand, Supply, Unit, SupplyItem, Packaging, Product


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DatatablesFilterBackend]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class PackagingViewSet(viewsets.ModelViewSet):
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    queryset = Supply.objects.all().annotate(
        num_items=Count('product__supplyitem', distinct=True, filter=Q(product__supplyitem__checkout_date=None)),
        order_value=Case(
            When(min_count=None, num_items=0, then=Value(-2)),
            When(min_count=None, num_items__gt=0, then=Value(-1)),
            When(min_count__gte=0, num_items=0, then=Value(0)),
            When(min_count__gte=0, num_items__gt=0, num_items__lt=F('min_count'), then=Value(1)),
            When(min_count__gt=0, num_items__gte=F('min_count'), then=Value(2)),
            default=Value(-2),
            output_field=IntegerField()
        )
    )
    serializer_class = SupplySerializer
    filter_backends = [filters.DatatablesFilterBackend]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().annotate(
        num_items=Count('supplyitem', distinct=True, filter=Q(supplyitem__checkout_date=None)),
        order_value=Case(
            When(min_count=None, num_items=0, then=Value(-2)),
            When(min_count=None, num_items__gt=0, then=Value(-1)),
            When(min_count__gte=0, num_items=0, then=Value(0)),
            When(min_count__gte=0, num_items__gt=0, num_items__lt=F('min_count'), then=Value(1)),
            When(min_count__gt=0, num_items__gte=F('min_count'), then=Value(2)),
            default=Value(-2),
            output_field=IntegerField()
        )
    )
    serializer_class = ProductSerializer
    filter_backends = [filters.DatatablesFilterBackend]


class SupplyItemViewSet(viewsets.ModelViewSet):
    queryset = SupplyItem.objects.filter(checkout_date=None)
    serializer_class = SupplyItemSerializer
    filter_backends = [filters.DatatablesFilterBackend]
