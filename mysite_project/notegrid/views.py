from django.views.generic.base import TemplateView


class NoteGridView(TemplateView):
    template_name = "notegrid/grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description = [
            """Page under construction.""",
            """You may recognize these dots as <a href=https://sites.google.com/site/davidrcanright/music-articles/har-mel-diag>Harmonic Melodic Diagrams</a>.  I want to make an app that accepts a midi file and outputs a visualization of notes on this grid in realtime.  No ETA.""",
        ]
        context["description"] = description
        return context
