from django.shortcuts import render
from books.models import Book
# from django.template.loader import get_template
# from django.http import HttpResponse, Http404


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    try:
        search_string = request.GET['q']
    except KeyError:
        return render(request, 'books/search_form.html', {'error': False})

    # because request.GET will give an empty string, if the passed in variable is empty
    if not search_string:
        return render(request, 'books/search_form.html', {'error': True})

    # verbose step-by-step of the magic render shortcut
    books_queryset = Book.objects.filter(title__icontains=search_string)
    # results_template = get_template('books/search_results.html')
    # context = {'books': books_queryset, 'query': search_string}
    # SafeText = results_template.render(context)
    # return HttpResponse(SafeText)

    # more and more succinct but more magic ways of saying this
    # t = get_template('books/search_results.html')
    # return render(request, t, context)

    # most magic & succinct way
    temp_stuff = render(request, 'books/search_results.html',
        {'books': books_queryset, 'query': search_string})
    print(temp_stuff._container)
    return temp_stuff
    # return render(request, 'books/search_results.html',
                  # {'books': books_queryset, 'query': search_string})