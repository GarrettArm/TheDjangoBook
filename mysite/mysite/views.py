from django.http import HttpResponse

from datetime import datetime


def hello(request):
    return HttpResponse('Hello world')


def current_datetime(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(dir(current_time))
    html = "<html><body>It is now {} </body></html>".format(current_time)
    return HttpResponse(html)
