from django.views.generic.base import TemplateView


class NoteGridView(TemplateView):
    template_name = 'notegrid/grid.html'
