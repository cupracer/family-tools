from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_modal_forms.mixins import PopRequestMixin
from django import forms
from django.forms import TextInput, NumberInput, CheckboxInput, ModelChoiceField
from django_select2.forms import ModelSelect2Widget
from .models import Category, Brand, Supply, Unit, SupplyItem, Packaging, Product


class CategorySelect2Widget(ModelSelect2Widget):
    model = Category
    search_fields = [
        'name__icontains'
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
        'name__icontains'
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
        'name__icontains'
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
        'name__icontains'
    ]


class SupplyForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('name', 'category', 'min_count')
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
            'min_count': NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class SupplySelect2Widget(ModelSelect2Widget):
    model = Supply
    search_fields = [
        'name__icontains',
    ]


class ProductForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('supply', 'name', 'brand', 'ean', 'unit', 'amount', 'packaging', 'bio_label', 'min_count')
        widgets = {
            'supply': SupplySelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                }
            ),
            'brand': BrandSelect2Widget(
                attrs={
                    'class': 'form-control',
                    'data-minimum-input-length': 0,
                }
            ),
            'ean': TextInput(
                attrs={
                    'class': 'form-control',
                },
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


class ProductSelect2Widget(ModelSelect2Widget):
    model = Product
    search_fields = [
        'name__icontains',
        'supply__name__icontains',
        'brand__name__icontains',
        'ean__contains'
    ]


class SupplyItemForm(PopRequestMixin, forms.ModelForm):
    purchase_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=DatePickerInput(
            format='%d.%m.%Y',
            options={
                'locale': 'de'
            },
        ),
    )
    best_before_date = forms.DateField(
        required=False,
        label="MHD",
        input_formats=['%d.%m.%Y'],
        widget=DatePickerInput(
            format='%d.%m.%Y',
            options={
                'locale': 'de',
                'useCurrent': False
            },
        ),
    )
    product = ModelChoiceField(
        queryset=Product.objects.all(),
        widget=ProductSelect2Widget(
            attrs={
                'class': 'form-control',
                'data-minimum-input-length': 0,
                'autofocus': 'autofocus',
            }
        )
    )

    class Meta:
        model = SupplyItem
        fields = ('product', 'purchase_date', 'best_before_date',)


class SupplyItemCreateForm(SupplyItemForm):
    count = forms.IntegerField(
        initial=1,
        widget=NumberInput(
            attrs={
                'class': 'form-control',
            }
        ))

    class Meta(SupplyItemForm.Meta):
        fields = SupplyItemForm.Meta.fields + ('count',)
