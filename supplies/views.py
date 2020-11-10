from copy import copy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib import messages
from guardian.mixins import PermissionRequiredMixin as GuardianPermissionRequiredMixin

from .forms import BrandForm, CategoryForm, SupplyForm, SupplyItemForm, SupplyItemCreateForm
from .models import Brand, Category, Supply, SupplyItem


class CategoryIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Category
    context_object_name = 'categories'
    template_name = 'supplies/categories/list.html'
    permission_required = 'supplies.view_category'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Categories'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'categories'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('supplies.add_category')
        })


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'supplies/categories/new.html'
    form_class = CategoryForm
    permission_required = 'supplies.add_category'
    success_message = 'Success: category was created.'
    success_url = reverse_lazy('supplies_category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create category'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'categories'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'supplies/categories/edit.html'
    permission_required = 'supplies.change_category'
    success_message = 'Success: Category was updated.'
    success_url = reverse_lazy('supplies_category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Edit category'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'categories'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class CategoryDeleteView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'supplies/categories/delete.html'
    permission_required = 'supplies.delete_category'
    success_message = 'Success: Category was deleted.'
    error_message = 'Error: Could not delete category.'
    success_url = reverse_lazy('supplies_category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Delete category'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'categories'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(self.request, self.error_message + ' (still in use)')
            return HttpResponseRedirect(success_url)


class BrandIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'supplies/brands/list.html'
    permission_required = 'supplies.view_brand'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Brands'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'brands'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('supplies.add_brand')
        })


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'supplies/brands/new.html'
    form_class = BrandForm
    permission_required = 'supplies.add_brand'
    success_message = 'Success: brand was created.'
    success_url = reverse_lazy('brand_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create brand'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'brands'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BrandUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'supplies/brands/edit.html'
    permission_required = 'supplies.change_brand'
    success_message = 'Success: brand was updated.'
    success_url = reverse_lazy('brand_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Edit brand'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'brands'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Brand
    form_class = BrandForm
    template_name = 'supplies/brands/delete.html'
    permission_required = 'supplies.delete_brand'
    success_message = 'Success: brand was deleted.'
    error_message = 'Error: Could not delete brand.'
    success_url = reverse_lazy('brand_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Delete brand'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'brands'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(self.request, self.error_message + ' (still in use)')
            return HttpResponseRedirect(success_url)


class SupplyIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Supply
    context_object_name = 'supplies'
    template_name = 'supplies/supplies/list.html'
    permission_required = 'supplies.view_supply'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Supplies'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supplies'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('supplies.add_supply')
        })


class SupplyCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'supplies/supplies/new.html'
    form_class = SupplyForm
    permission_required = 'supplies.add_supply'
    success_message = 'Success: supply was created.'
    success_url = reverse_lazy('supply_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create supply'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supplies'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SupplyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Supply
    form_class = SupplyForm
    template_name = 'supplies/supplies/edit.html'
    permission_required = 'supplies.change_supply'
    success_message = 'Success: supply was updated.'
    success_url = reverse_lazy('supply_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Edit supply'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supplies'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class SupplyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Supply
    form_class = SupplyForm
    template_name = 'supplies/supplies/delete.html'
    permission_required = 'supplies.delete_supply'
    success_message = 'Success: supply was deleted.'
    error_message = 'Error: Could not delete supply.'
    success_url = reverse_lazy('supply_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Delete supply'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supplies'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(self.request, self.error_message + ' (still in use)')
            return HttpResponseRedirect(success_url)


class SupplyItemIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = SupplyItem
    context_object_name = 'supply_items'
    template_name = 'supplies/supply_items/list.html'
    permission_required = 'supplies.view_supplyitem'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Supply items'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supply_items'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('supplies.add_supplyitem')
        })


class SupplyItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'supplies/supply_items/new.html'
    form_class = SupplyItemCreateForm
    permission_required = 'supplies.add_supplyitem'
    success_message = 'Success: supply item was created.'
    success_url = reverse_lazy('supply_item_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create supply item'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supply_items'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        for x in range(1, form.cleaned_data['count']+1):
            form.instance.pk = None
            self.object = form.save()

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return HttpResponseRedirect(self.get_success_url())


class SupplyItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = SupplyItem
    form_class = SupplyItemForm
    template_name = 'supplies/supply_items/edit.html'
    permission_required = 'supplies.change_supplyitem'
    success_message = 'Success: supply item was updated.'
    success_url = reverse_lazy('supply_item_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Edit supply item'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supply_items'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class SupplyItemCloneView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = SupplyItem
    form_class = SupplyItemCreateForm
    template_name = 'supplies/supply_items/new.html'
    permission_required = 'supplies.add_supplyitem'
    success_message = 'Success: supply item was created.'
    success_url = reverse_lazy('supply_item_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create supply item'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supply_items'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        for x in range(1, form.cleaned_data['count']+1):
            form.instance.pk = None
            self.object = form.save()

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return HttpResponseRedirect(self.get_success_url())


class SupplyItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = SupplyItem
    form_class = SupplyItemForm
    template_name = 'supplies/supply_items/delete.html'
    permission_required = 'supplies.delete_supplyitem'
    success_message = 'Success: supply item was deleted.'
    error_message = 'Error: Could not delete supply item.'
    success_url = reverse_lazy('supply_item_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Delete supply items'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'supply_items'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(self.request, self.error_message + ' (still in use)')
            return HttpResponseRedirect(success_url)