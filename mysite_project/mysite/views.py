import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class FrontView(TemplateView):
    template_name = 'mysite/frontpage.html'


def hello(request):
    return HttpResponse('Hello world')


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    context = {'current_datestuff': current_time}
    template_path = os.path.join('dateapp', 'current_datetime.html')
    return render(request, template_path, context)


def hours_ahead(request, hours=0):
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=hours)
    context = {'hour_offset': hours, 'incremented_time': incremented_time, }
    template_path = os.path.join('dateapp', 'future_datetime.html')
    return render(request, template_path, context)


def add_nonsense(request, year=0, month=0, day=0):
    sum = int(year) + int(month) + int(day)
    text = "Year: {}, Month: {}, Day {}, which add to {}".format(year, month, day, sum)
    return HttpResponse(text)
