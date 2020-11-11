from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_modal_forms.mixins import PopRequestMixin
from django import forms
from django.forms import TextInput, NumberInput, CheckboxInput
from django_select2.forms import ModelSelect2Widget
from .models import Category, Brand, Supply, Unit, SupplyItem, Packaging


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


class BrandSelect2Widget(ModelSelect2Widget):
    model = Category
    search_fields = [
        'name__istartswith'
    ]


class BrandForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
        }


class PackagingSelect2Widget(ModelSelect2Widget):
    model = Packaging
    search_fields = [
        'name__istartswith'
    ]


class PackagingForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Packaging
        fields = ('name',)
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
        }


class UnitSelect2Widget(ModelSelect2Widget):
    model = Unit
    search_fields = [
        'name__istartswith'
    ]


class SupplyForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('name', 'category', 'brand', 'unit', 'amount', 'packaging', 'bio_label', 'min_count')
        widgets = {
            'name': TextInput(attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
            'category': CategorySelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'brand': BrandSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'unit': UnitSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'amount': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'packaging': PackagingSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'bio_label': CheckboxInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'min_count': NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class SupplySelect2Widget(ModelSelect2Widget):
    model = Supply
    search_fields = [
        'name__icontains'
    ]


class SupplyItemForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = SupplyItem
        fields = ('supply', 'purchase_date', 'best_before_date',)
        widgets = {
            'supply': SupplySelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'purchase_date': DatePickerInput(
                options={
                    'locale': 'de'
                }
            ),
            'best_before_date': DatePickerInput(
                options={
                    'locale': 'de',
                    'useCurrent': False
                }
            ),
        }


class SupplyItemCreateForm(SupplyItemForm):
    count = forms.IntegerField(
        initial=1,
        widget=NumberInput(
            attrs={
                'class': 'form-control'
            }
        ))

    class Meta(SupplyItemForm.Meta):
        fields = SupplyItemForm.Meta.fields + ('count',)
