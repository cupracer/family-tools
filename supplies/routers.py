from rest_framework import routers
from django.urls import path, include
from .viewsets import CategoryViewSet, BrandViewSet, SupplyViewSet, UnitViewSet, SupplyItemViewSet, PackagingViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('brands', BrandViewSet)
router.register('units', UnitViewSet)
router.register('packagings', PackagingViewSet)
router.register('supplies', SupplyViewSet)
router.register('supply_items', SupplyItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
