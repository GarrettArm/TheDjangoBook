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
    # template_file = 'books/search_results.html'
    # template_text = get_template(template_file)
    # context = {'books': books_queryset, 'query': search_string}
    # SafeText = template_text.render(context)
    # return HttpResponse(SafeText)

    # more and more succinct but more magic ways of saying this
    # t = get_template('books/search_results.html')
    # return render(request, t, context)

    # most magic & succinct way
    return render(request, 'books/search_results.html',
                  {'books': books_queryset, 'query': search_string})
