from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = "main/base.html"
    site = {
        'name': 'TeamTools',
        'page_title': 'Start'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'site': self.site
        })
