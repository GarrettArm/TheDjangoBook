from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse('Hello world')


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return render(request, 'current_datetime.html', {'current_datestuff': current_time})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hours, it will be {}</body></html>".format(offset, incremented_time)
    return HttpResponse(html)
