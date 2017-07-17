from django.shortcuts import render
from django.http import HttpResponse


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    search_string = request.GET['q']
    if search_string:
        message = 'You searched for: {}'.format(search_string)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
