from rest_framework import routers
from django.urls import path, include
from .viewsets import CategoryViewSet, BrandViewSet, SupplyViewSet, UnitViewSet, SupplyItemViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('brands', BrandViewSet)
router.register('units', UnitViewSet)
router.register('supplies', SupplyViewSet)
router.register('supply_items', SupplyItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
