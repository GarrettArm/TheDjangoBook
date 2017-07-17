from django.http import HttpResponse, Http404
from django.shortcuts import render

import datetime
import os


def hello(request):
    return HttpResponse('Hello world')


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    context = {'current_datestuff': current_time}
    template_path = os.path.join('dateapp', 'current_datetime.html')
    return render(request, template_path, context)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = {'hour_offset': offset, 'incremented_time': incremented_time, }
    template_path = os.path.join('dateapp', 'future_datetime.html')
    return render(request, template_path, context)
