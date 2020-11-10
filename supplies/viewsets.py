from rest_framework import viewsets
from rest_framework_datatables import filters

from .serializers import CategorySerializer, BrandSerializer, SupplySerializer, UnitSerializer, SupplyItemSerializer
from .models import Category, Brand, Supply, Unit, SupplyItem


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


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    filter_backends = [filters.DatatablesFilterBackend]


class SupplyItemViewSet(viewsets.ModelViewSet):
    queryset = SupplyItem.objects.all()
    serializer_class = SupplyItemSerializer
    filter_backends = [filters.DatatablesFilterBackend]
