from django.contrib.auth.mixins import LoginRequiredMixin
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
