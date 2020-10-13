from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "main/base.html"
    site = {
        'name': 'FamilyTools',
        'page_title': 'Start'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site
        })


class MainLoginView(LoginView):
    site = {
        'name': 'FamilyTools',
        'page_title': 'Login'
    }
    nav = {
        'first_level': 'main',
        'second_level': 'login'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site'] = self.site
        context['nav'] = self.nav
        return context
