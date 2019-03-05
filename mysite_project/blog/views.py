from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for i in context['object_list']:
            i.text_as_list = self.split_to_paragraphs(i.text)
        description = [
          "A description",
        ]
        context['description'] = description
        return context

    def split_to_paragraphs(self, text):
        text_list = f"{text[:300]}...".split('\n')
        return text_list


class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['object'].text_as_list = self.split_to_paragraphs(context['object'].text)
        description = [
          "Another description",
        ]
        context['description'] = description
        return context

    def split_to_paragraphs(self, text):
        text_list = text.split('\n')
        return text_list