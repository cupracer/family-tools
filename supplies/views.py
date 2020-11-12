from copy import copy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib import messages
from django.views.generic.detail import BaseDetailView
from guardian.mixins import PermissionRequiredMixin as GuardianPermissionRequiredMixin
from django.http import JsonResponse
import todoist
from rest_framework.response import Response
from todoist.api import SyncError
from rest_framework import generics

from family_tools import settings
from .forms import BrandForm, CategoryForm, SupplyForm, SupplyItemForm, SupplyItemCreateForm, PackagingForm
from .models import Brand, Category, Supply, SupplyItem, Packaging
from .serializers import SupplyItemSerializer, SupplySerializer


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


class PackagingIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Packaging
    context_object_name = 'packagings'
    template_name = 'supplies/packagings/list.html'
    permission_required = 'supplies.view_packaging'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Packagings'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'packagings'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('supplies.add_packaging')
        })


class PackagingCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'supplies/packagings/new.html'
    form_class = PackagingForm
    permission_required = 'supplies.add_packaging'
    success_message = 'Success: packaging was created.'
    success_url = reverse_lazy('packaging_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Create packaging'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'packagings'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PackagingUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Packaging
    form_class = PackagingForm
    template_name = 'supplies/packagings/edit.html'
    permission_required = 'supplies.change_packaging'
    success_message = 'Success: packaging was updated.'
    success_url = reverse_lazy('packaging_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Edit packaging'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'packagings'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class PackagingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Packaging
    form_class = PackagingForm
    template_name = 'supplies/packagings/delete.html'
    permission_required = 'supplies.delete_packaging'
    success_message = 'Success: packaging was deleted.'
    error_message = 'Error: Could not delete packaging.'
    success_url = reverse_lazy('packaging_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Supplies',
        'page_title': 'Delete packaging'
    }
    nav = {
        'first_level': 'supplies',
        'second_level': 'packagings'
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

    def get(self, request, *args, **kwargs):
        site = {
            'name': 'FamilyTools',
            'app_title': 'Supplies',
            'page_title': 'Supplies'
        }
        nav = {
            'first_level': 'supplies',
            'second_level': 'supplies'
        }
        datatables_path = '/api/supplies/supplies/?format=datatables'

        context = {
            'site': site,
            'nav': nav,
            'can_add': self.request.user.has_perm('supplies.add_supply'),
            'use_todoist': True if self.request.user.todoist_api_key else False,
            'datatables_path': datatables_path
        }

        if 'supply_id' in kwargs:
            supply = Supply.objects.get(id=kwargs['supply_id'])
            context['datatables_path'] = '/supplies/supplies/by_id/' + \
                 str(kwargs['supply_id']) + '/json/?format=datatables'
            context['site']['page_title'] = 'Supplies (filtered by "' + supply.name + '")'

        return render(request, self.template_name, context)


# I wasted several hours for this sh*tty class!
# Without that get() method and using "many=True" the serializer returned an empty result only.
# I still don't understand why this all is needed, because "housekeeping_book/views.py" doesn't need it. :-(
class SupplyByIdJson(generics.ListAPIView):
    serializer_class = SupplySerializer()

    def get_queryset(self):
        supply_id = self.kwargs['supply_id']
        return Supply.objects.filter(pk=supply_id).annotate(
            num_items=Count('supplyitem', distinct=True))

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SupplySerializer(queryset, many=True)
        return Response(serializer.data)


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


class SupplyAddToTodoistView(LoginRequiredMixin, PermissionRequiredMixin, BaseDetailView):
    permission_required = 'supplies.view_supply'
    queryset = Supply.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        try:
            if not self.request.user.todoist_api_key:
                raise Exception('Todoist API key is missing.')

            api = todoist.TodoistAPI(self.request.user.todoist_api_key)
            item = api.items.add(self.object.name, project_id=settings.TODOIST_PROJECT_ID)
            item.move(section_id=settings.TODOIST_SECTION_ID)
            api.commit()
        except KeyError:
            return JsonResponse({
                "status": "error",
                "message": "key error"
            })
        except SyncError:
            return JsonResponse({
                "status": "error",
                "message": "sync error"
            })
        except TypeError:
            return JsonResponse({
                "status": "error",
                "message": "type error"
            })
        except Exception as inst:
            return JsonResponse({
                "status": "error",
                "message": inst.args
            })

        return JsonResponse({
            "status": "success",
            "message": self.object.name
        })


class SupplyItemIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = SupplyItem
    context_object_name = 'supply_items'
    template_name = 'supplies/supply_items/list.html'
    permission_required = 'supplies.view_supplyitem'

    def get(self, request, *args, **kwargs):
        site = {
            'name': 'FamilyTools',
            'app_title': 'Supplies',
            'page_title': 'Supply items'
        }
        nav = {
            'first_level': 'supplies',
            'second_level': 'supply_items'
        }
        datatables_path = '/api/supplies/supply_items/?format=datatables'

        context = {
            'site': site,
            'nav': nav,
            'can_add': self.request.user.has_perm('supplies.add_supplyitem'),
            'datatables_path': datatables_path
        }

        if 'supply_id' in kwargs:
            supply = Supply.objects.get(id=kwargs['supply_id'])
            context['datatables_path'] = '/supplies/supply_items/by_supply/' + \
                 str(kwargs['supply_id']) + '/json/?format=datatables'
            context['site']['page_title'] = 'Supply items (filtered by supply "' + supply.name + '")'

        return render(request, self.template_name, context)


# I wasted several hours for this sh*tty class!
# Without that get() method and using "many=True" the serializer returned an empty result only.
# I still don't understand why this all is needed, because "housekeeping_book/views.py" doesn't need it. :-(
class SupplyItemBySupplyJson(generics.ListAPIView):
    serializer_class = SupplyItemSerializer()

    def get_queryset(self):
        supply_id = self.kwargs['supply_id']
        return SupplyItem.objects.filter(supply_id=supply_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SupplyItemSerializer(queryset, many=True)
        return Response(serializer.data)


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
