from django.shortcuts import render
from books.models import Book


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    try:
        search_string = request.GET['q']
    except KeyError:
        return render(request, 'books/search_form.html', {'error': False})

    if not search_string:
        return render(request, 'books/search_form.html', {'error': True})

    books = Book.objects.filter(title__icontains=search_string)
    return render(request, 'books/search_results.html',
                  {'books': books, 'query': search_string})
