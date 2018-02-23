from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book


class searchView(FormView):
    template_name = 'books/book_search.html'
    form_class = BookForm
    success_url = reverse_lazy('books:class_search')

    def get(self, request, *ags, **kwargs):
        if not request.GET:
            form = self.form_class()
            response = render(request, self.template_name, {'form': form})
            return response
        form = self.form_class(request.GET)
        if form.is_valid():
            query = form['title'].value()
            try:
                books_queryset = Book.objects.filter(title__icontains=query)
            except Book.DoesNotExist:
                books_queryset = None
            response = render(request, self.template_name, {'form': form, 'books': books_queryset, 'query': query, })
            return response
        else:
            form = self.form_class()
            response = render(request, self.template_name, {'form': form})
            return response
