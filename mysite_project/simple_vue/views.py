import datetime

from django.shortcuts import render
from django.views.generic import TemplateView


class SimpleVueView(TemplateView):
    template_name = 'simple_vue/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['current_datestuff'] = current_time
        counters = [1, 2, 3, 4]
        context['counters'] = counters
        return context
