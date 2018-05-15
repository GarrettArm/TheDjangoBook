import datetime

from django.views.generic import TemplateView


class FrontView(TemplateView):
    template_name = 'mysite/frontpage.html'


class CurrentDateView(TemplateView):
    template_name = 'dateapp/current_datetime.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['current_datestuff'] = current_time
        return context
