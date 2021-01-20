from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_modal_forms.mixins import PopRequestMixin
from django import forms
from django.contrib.auth.models import Group
from django.forms import TextInput, NumberInput
from django_select2.forms import ModelSelect2Widget

from main.models import User
from .models import AccountHolder, Category, Booking, PeriodicBooking


class AccountHolderSelect2Widget(ModelSelect2Widget):
    model = AccountHolder
    search_fields = [
        'name__icontains'
    ]


class AccountHolderForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = AccountHolder
        fields = ('name',)
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
        }


class CategorySelect2Widget(ModelSelect2Widget):
    model = Category
    search_fields = [
        'name__istartswith'
    ]


class CategoryForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
        }


class BookingForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('category', 'account_holder', 'booking_date', 'description', 'amount')
        widgets = {
            'category': CategorySelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'account_holder': AccountHolderSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'booking_date': DatePickerInput(
                format='%d.%m.%Y',
                options={
                    'locale': 'de'
                }
            ),
            'description': TextInput(attrs={'class': 'form-control'}),
            'amount': NumberInput(attrs={'class': 'form-control'}),
        }


class PeriodicBookingForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = PeriodicBooking
        fields = ('category', 'account_holder', 'booking_day_of_month', 'description', 'amount',
                  'start_date', 'end_date', 'interval')
        widgets = {
            'category': CategorySelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'account_holder': AccountHolderSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'booking_day_of_month': NumberInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'amount': NumberInput(attrs={'class': 'form-control'}),
            'start_date': DatePickerInput(
                format='%d.%m.%Y',
                options={
                    'locale': 'de'
                }
            ),
            'end_date': DatePickerInput(
                format='%d.%m.%Y',
                options={
                    'locale': 'de'
                }
            ),
            'interval': NumberInput(attrs={'class': 'form-control'}),
        }


class UserSelect2Widget(ModelSelect2Widget):
    model = User
    membersGroup = Group.objects.get(name='members')
    queryset = User.objects.filter(groups=membersGroup)
    search_fields = [
        'name__icontains'
    ]


class CategoryTotalPerMonthForm(forms.Form):
    user = forms.IntegerField(widget=UserSelect2Widget(
        attrs={'class': 'form-control', 'data-minimum-input-length': 0}), required=False)
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    include_periodic_bookings = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    spread_amount = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    include_dynamic_bookings = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
