from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    search_string = request.GET['q']
    if search_string:
        books = Book.objects.filter(title__icontains=search_string)
        return render(request, 'books/search_results.html',
                      {'books': books, 'query': search_string})
    else:
        return HttpResponse('Please submit a search term.')
