from django.http import HttpResponse, Http404
from django.template.loader import get_template
import datetime


def hello(request):
    return HttpResponse('Hello world')


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    t = get_template('current_datetime.html')
    html = t.render({'current_date': current_time})
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hours, it will be {}</body></html>".format(offset, incremented_time)
    return HttpResponse(html)
