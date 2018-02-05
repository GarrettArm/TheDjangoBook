import datetime

from django.shortcuts import render
from django.views.generic import TemplateView


class FrontView(TemplateView):
    template_name = 'mysite/frontpage.html'


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    context = {'current_datestuff': current_time}
    template_path = 'dateapp/current_datetime.html'
    return render(request, template_path, context)
