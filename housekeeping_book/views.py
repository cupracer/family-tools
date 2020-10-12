import random
import string
from datetime import datetime, date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib import messages
import simplejson
from guardian.mixins import PermissionRequiredMixin as GuardianPermissionRequiredMixin
from guardian.shortcuts import assign_perm, remove_perm

from main.models import User
from .forms import AccountHolderForm, CategoryForm, BookingForm, PeriodicBookingForm, CategoryTotalPerMonthForm
from .models import AccountHolder, Category, Booking, PeriodicBooking


class AccountHolderIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = AccountHolder
    context_object_name = 'account_holders'
    template_name = 'housekeeping_book/account_holders/list.html'
    permission_required = 'housekeeping_book.view_accountholder'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Account holders'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'account_holders'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('housekeeping_book.add_accountholder')
        })


class AccountHolderCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'housekeeping_book/account_holders/new.html'
    form_class = AccountHolderForm
    permission_required = 'housekeeping_book.add_accountholder'
    success_message = 'Success: account holder was created.'
    success_url = reverse_lazy('account_holder_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Create account holder'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'account_holders'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountHolderUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = AccountHolder
    form_class = AccountHolderForm
    template_name = 'housekeeping_book/account_holders/edit.html'
    permission_required = 'housekeeping_book.change_accountholder'
    success_message = 'Success: Account holder was updated.'
    success_url = reverse_lazy('account_holder_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Edit account holder'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'account_holders'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class AccountHolderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = AccountHolder
    form_class = AccountHolderForm
    template_name = 'housekeeping_book/account_holders/delete.html'
    permission_required = 'housekeeping_book.delete_accountholder'
    success_message = 'Success: Account holder was deleted.'
    error_message = 'Error: Could not delete account holder.'
    success_url = reverse_lazy('account_holder_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Delete account holder'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'account_holders'
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


class CategoryIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Category
    context_object_name = 'categories'
    template_name = 'housekeeping_book/categories/list.html'
    permission_required = 'housekeeping_book.view_category'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Categories'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'categories'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('housekeeping_book.add_category')
        })


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'housekeeping_book/categories/new.html'
    form_class = CategoryForm
    permission_required = 'housekeeping_book.add_category'
    success_message = 'Success: category was created.'
    success_url = reverse_lazy('category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Create category'
    }
    nav = {
        'first_level': 'housekeeping_book',
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
    template_name = 'housekeeping_book/categories/edit.html'
    permission_required = 'housekeeping_book.change_category'
    success_message = 'Success: Category was updated.'
    success_url = reverse_lazy('category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Edit category'
    }
    nav = {
        'first_level': 'housekeeping_book',
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
    template_name = 'housekeeping_book/categories/delete.html'
    permission_required = 'housekeeping_book.delete_category'
    success_message = 'Success: Category was deleted.'
    error_message = 'Error: Could not delete category.'
    success_url = reverse_lazy('category_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Delete category'
    }
    nav = {
        'first_level': 'housekeeping_book',
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


class BookingIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'housekeeping_book/bookings/list.html'
    permission_required = 'housekeeping_book.view_booking'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Dynamic bookings'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'bookings'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('housekeeping_book.add_booking')
        })


class BookingCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'housekeeping_book/bookings/new.html'
    permission_required = 'housekeeping_book.add_booking'
    success_message = 'Success: Booking was created.'
    success_url = reverse_lazy('booking_new')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Create dynamic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'bookings'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()

        assign_perm(self.model._meta.app_label + '.' + 'view_' + self.model._meta.model_name,
                    self.request.user,  self.object)
        assign_perm(self.model._meta.app_label + '.' + 'change_' + self.model._meta.model_name,
                    self.request.user, self.object)
        assign_perm(self.model._meta.app_label + '.' + 'delete_' + self.model._meta.model_name,
                    self.request.user, self.object)

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return HttpResponseRedirect(self.get_success_url())


class BookingUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'housekeeping_book/bookings/edit.html'
    permission_required = 'housekeeping_book.change_booking'
    success_message = 'Success: Dynamic booking was updated.'
    success_url = reverse_lazy('booking_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Edit dynamic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'bookings'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context


class BookingDeleteView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Booking
    form_class = BookingForm
    template_name = 'housekeeping_book/bookings/delete.html'
    permission_required = 'housekeeping_book.delete_booking'
    success_message = 'Success: Dynamic booking was deleted.'
    error_message = 'Error: Could not delete dynamic booking.'
    success_url = reverse_lazy('booking_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Delete dynamic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'bookings'
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


class PeriodicBookingIndex(LoginRequiredMixin, GuardianPermissionRequiredMixin, generic.TemplateView):
    template_name = 'housekeeping_book/periodic_bookings/list.html'
    permission_required = 'housekeeping_book.view_periodicbooking'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Periodic bookings'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'periodic_bookings'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site,
            'nav': self.nav,
            'can_add': self.request.user.has_perm('housekeeping_book.add_periodicbooking')
        })


class PeriodicBookingCreateView(LoginRequiredMixin, PermissionRequiredMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    model = PeriodicBooking
    form_class = PeriodicBookingForm
    template_name = 'housekeeping_book/periodic_bookings/new.html'
    permission_required = 'housekeeping_book.add_periodicbooking'
    success_message = 'Success: Periodic booking was created.'
    success_url = reverse_lazy('periodic_booking_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Create periodic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'periodic_bookings'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        form.instance.identifier = r
        form.instance.start_date = date(form.instance.start_date.year, form.instance.start_date.month, 1)
        if form.instance.end_date:
            form.instance.end_date = \
                date(form.instance.end_date.year,
                     (form.instance.end_date + relativedelta(months=+1)).month, 1) + relativedelta(days=-1)

        self.object = form.save()

        assign_perm(self.model._meta.app_label + '.' + 'view_' + self.model._meta.model_name,
                    self.request.user,  self.object)
        assign_perm(self.model._meta.app_label + '.' + 'change_' + self.model._meta.model_name,
                    self.request.user, self.object)
        assign_perm(self.model._meta.app_label + '.' + 'delete_' + self.model._meta.model_name,
                    self.request.user, self.object)

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return HttpResponseRedirect(self.get_success_url())




class PeriodicBookingUpdateView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = PeriodicBooking
    form_class = PeriodicBookingForm
    template_name = 'housekeeping_book/periodic_bookings/edit.html'
    permission_required = 'housekeeping_book.change_periodicbooking'
    success_message = 'Success: Periodic booking was updated.'
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Edit periodic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'periodic_bookings'
    }

    def get_success_url(self, **kwargs):
        return reverse_lazy('periodic_booking_edit', args=(self.object.id,))

    def form_valid(self, form):
        periodic_booking = form.save(commit=False)
        periodic_booking.last_update = datetime.now()
        periodic_booking.save()
        return super().form_valid(form)


class PeriodicBookingDeleteView(LoginRequiredMixin, GuardianPermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = PeriodicBooking
    form_class = PeriodicBookingForm
    template_name = 'housekeeping_book/periodic_bookings/delete.html'
    permission_required = 'housekeeping_book.delete_periodicbooking'
    success_message = 'Success: Periodic booking was deleted.'
    error_message = 'Error: Could not delete periodic booking.'
    success_url = reverse_lazy('periodic_booking_index')
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Delete periodic booking'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'periodic_bookings'
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


def month_year_iter(start_month, start_year, end_month, end_year):
    ym_start = 12 * start_year + start_month - 1
    ym_end = 12 * end_year + end_month - 1
    for ym in range(ym_start, ym_end):
        y, m = divmod(ym, 12)
        yield y, m + 1


class StatisticsCategoryTotalPerMonth(LoginRequiredMixin, generic.TemplateView):
    template_name = 'housekeeping_book/statistics/category_total_per_month.html'
    year = date.today().year
    user = None
    include_periodic_bookings = True
    spread_amount = False
    include_dynamic_bookings = True
    site = {
        'name': 'FamilyTools',
        'app_title': 'Housekeeping Book',
        'page_title': 'Statistics'
    }
    nav = {
        'first_level': 'housekeeping_book',
        'second_level': 'statistics_category_totals_per_month'
    }
    form = CategoryTotalPerMonthForm(
        initial={
            'user': user,
            'year': year,
            'include_periodic_bookings': include_periodic_bookings,
            'spread_amount': spread_amount,
            'include_dynamic_bookings': include_dynamic_bookings
        }
    )

    def get(self, request, *args, **kwargs):
        return self.renderer(self.form)

    def post(self, request, *args, **kwargs):
        form = CategoryTotalPerMonthForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd.get('user'):
                self.user = User.objects.get(id=cd.get('user'))
            if cd.get('year'):
                self.year = cd.get('year')
            if cd.get('include_periodic_bookings'):
                self.include_periodic_bookings = cd.get('include_periodic_bookings')
            else:
                self.include_periodic_bookings = False
            if cd.get('spread_amount'):
                self.spread_amount = cd.get('spread_amount')
            else:
                self.spread_amount = False
            if cd.get('include_dynamic_bookings'):
                self.include_dynamic_bookings = cd.get('include_dynamic_bookings')
            else:
                self.include_dynamic_bookings = False

        return self.renderer(form)

    def renderer(self, form):
        data = []
        total_months = {'category': 'TOTAL'}

        for category in Category.objects.all():
            monthly_data = {
                'category': category.name
            }

            dynamic_bookings = None

            if self.include_dynamic_bookings:
                # fetch all dynamic booking at once for the chosen year (filter for months later)
                if self.user:
                    dynamic_bookings = Booking.objects.filter(
                        user=self.user, category=category, booking_date__year=self.year
                    )
                else:
                    dynamic_bookings = Booking.objects.filter(category=category, booking_date__year=self.year)

            for month in list(range(1, 13)):
                total = 0

                if month not in total_months.keys():
                    mtotal = {
                        month: 0
                    }
                    total_months.update(mtotal)

                # dynamic bookings

                if self.include_dynamic_bookings:

                    for booking in dynamic_bookings:
                        if booking.booking_date.month == month:
                            total += booking.amount

                            mtotal = {
                                month: total_months.get(month) + round(booking.amount)
                            }
                            total_months.update(mtotal)

                # periodic bookings

                if self.include_periodic_bookings:
                    if self.user:
                        periodic_bookings = PeriodicBooking.objects.filter(user=self.user, category=category)
                    else:
                        periodic_bookings = PeriodicBooking.objects.filter(category=category)

                    pbs = []

                    for periodic_booking in periodic_bookings:
                        interval_months = []
                        interval_date = periodic_booking.start_date

                        if periodic_booking.end_date:
                            loop_end_date = periodic_booking.end_date
                        else:
                            loop_end_date = date(self.year, 12, 31)

                        if self.spread_amount:
                            amount = periodic_booking.amount / periodic_booking.interval
                            while interval_date <= loop_end_date:
                                if interval_date.year == self.year and interval_date.month == month:
                                    interval_months.append(interval_date.month)
                                interval_date = interval_date + relativedelta(months=+1)
                        else:
                            amount = periodic_booking.amount
                            while interval_date <= loop_end_date:
                                if interval_date.year == self.year and interval_date.month == month:
                                    interval_months.append(interval_date.month)
                                interval_date = interval_date + relativedelta(months=periodic_booking.interval)

                        if month in interval_months:
                            last_day_of_month = (
                                    (date(self.year, month, 1) + relativedelta(months=+1)) + relativedelta(days=-1)).day
                            if periodic_booking.booking_day_of_month > last_day_of_month:
                                booking_date = date(self.year, month, last_day_of_month)
                            else:
                                booking_date = date(self.year, month, periodic_booking.booking_day_of_month)

                            periodic_booking_instance = Booking(
                                user=periodic_booking.user,
                                category=periodic_booking.category,
                                account_holder=periodic_booking.account_holder,
                                amount=amount,
                                description=periodic_booking.description,
                                parent_identifier=periodic_booking.identifier,
                                booking_date=booking_date
                            )
                            pbs.append(periodic_booking_instance)

                    for booking in pbs:
                        total += booking.amount

                        mtotal = {
                            month: total_months.get(month) + round(booking.amount)
                        }
                        total_months.update(mtotal)

                # total:

                if not total:
                    monthly_total = {
                        str(month): '-'
                    }
                else:
                    monthly_total = {
                        str(month): round(total)
                    }

                monthly_data.update(monthly_total)

            data.append(monthly_data)

        return render(
            self.request,
            self.template_name,
            {
                'site': self.site,
                'nav': self.nav,
                'form': form,
                'data': simplejson.dumps(data),
                'total': simplejson.dumps(total_months)
            }
        )
