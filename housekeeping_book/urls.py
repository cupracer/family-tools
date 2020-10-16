from django.urls import path
from . import views
from .views import BookingByAccountHolderJson, BookingByCategoryJson

urlpatterns = [
    path('accountholders/', views.AccountHolderIndex.as_view(), name='account_holder_index'),
    path('accountholders/new/', views.AccountHolderCreateView.as_view(), name='account_holder_new'),
    path('accountholders/<int:pk>/edit/', views.AccountHolderUpdateView.as_view(), name='account_holder_edit'),
    path('accountholders/<int:pk>/delete/', views.AccountHolderDeleteView.as_view(), name='account_holder_delete'),

    path('categories/', views.CategoryIndex.as_view(), name='category_index'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category_new'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('bookings/', views.BookingIndex.as_view(), name='booking_index'),
    path('bookings/new/', views.BookingCreateView.as_view(), name='booking_new'),
    path('bookings/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),

    path('bookings/by_account_holder/<int:account_holder_id>/', views.BookingIndex.as_view(), name='booking_by_account_holder_index'),
    path('bookings/by_account_holder/<int:account_holder_id>/json/', BookingByAccountHolderJson.as_view()),

    path('bookings/by_category/<int:category_id>/', views.BookingIndex.as_view(), name='booking_by_category_index'),
    path('bookings/by_category/<int:category_id>/json/', BookingByCategoryJson.as_view()),

    path('periodic_bookings/', views.PeriodicBookingIndex.as_view(), name='periodic_booking_index'),
    path('periodic_bookings/new/', views.PeriodicBookingCreateView.as_view(), name='periodic_booking_new'),
    path('periodic_bookings/<int:pk>/edit/', views.PeriodicBookingUpdateView.as_view(), name='periodic_booking_edit'),
    path('periodic_bookings/<int:pk>/delete/',
         views.PeriodicBookingDeleteView.as_view(), name='periodic_booking_delete'),

    path('statistics/', views.StatisticsCategoryTotalPerMonth.as_view(), name='statistics_category_totals_per_month'),
]
