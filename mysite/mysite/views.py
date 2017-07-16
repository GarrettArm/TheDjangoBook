from django.http import HttpResponse, Http404

import datetime


def hello(request):
    return HttpResponse('Hello world')


def current_datetime(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    html = "<html><body>It is now {} </body></html>".format(current_time)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hours, it will be {}</body></html>".format(offset, incremented_time)
    return HttpResponse(html)
