from django.urls import path
from . import views
from .views import SupplyItemBySupplyJson, SupplyByIdJson

urlpatterns = [
    path('categories/', views.CategoryIndex.as_view(), name='supplies_category_index'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category_new'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('brands/', views.BrandIndex.as_view(), name='brand_index'),
    path('brands/new/', views.BrandCreateView.as_view(), name='brand_new'),
    path('brands/<int:pk>/edit/', views.BrandUpdateView.as_view(), name='brand_edit'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    path('packagings/', views.PackagingIndex.as_view(), name='packaging_index'),
    path('packagings/new/', views.PackagingCreateView.as_view(), name='packaging_new'),
    path('packagings/<int:pk>/edit/', views.PackagingUpdateView.as_view(), name='packaging_edit'),
    path('packagings/<int:pk>/delete/', views.PackagingDeleteView.as_view(), name='packaging_delete'),

    path('supplies/', views.SupplyIndex.as_view(), name='supply_index'),
    path('supplies/new/', views.SupplyCreateView.as_view(), name='supply_new'),
    path('supplies/<int:pk>/edit/', views.SupplyUpdateView.as_view(), name='supply_edit'),
    path('supplies/<int:pk>/delete/', views.SupplyDeleteView.as_view(), name='supply_delete'),
    path('supplies/<int:pk>/todoist/', views.SupplyAddToTodoistView.as_view(), name='supply_todoist'),

    path('supplies/by_id/<int:supply_id>/', views.SupplyIndex.as_view()),
    path('supplies/by_id/<int:supply_id>/json/', SupplyByIdJson.as_view()),

    path('supply_items/', views.SupplyItemIndex.as_view(), name='supply_item_index'),
    path('supply_items/new/', views.SupplyItemCreateView.as_view(), name='supply_item_new'),
    path('supply_items/<int:pk>/edit/', views.SupplyItemUpdateView.as_view(), name='supply_item_edit'),
    path('supply_items/<int:pk>/delete/', views.SupplyItemDeleteView.as_view(), name='supply_item_delete'),
    path('supply_items/<int:pk>/clone/', views.SupplyItemCloneView.as_view(), name='supply_item_clone'),
    path('supply_items/<int:pk>/checkout/', views.SupplyItemCheckoutView.as_view(), name='supply_checkout'),
    path('supply_items/<int:pk>/checkin/', views.SupplyItemCheckinView.as_view(), name='supply_checkin'),

    path('supply_items/by_supply/<int:supply_id>/', views.SupplyItemIndex.as_view()),
    path('supply_items/by_supply/<int:supply_id>/json/', SupplyItemBySupplyJson.as_view()),
]
