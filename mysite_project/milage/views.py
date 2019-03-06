from django.views.generic import TemplateView
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework_xml.renderers import XMLRenderer

from .models import FuelEffeciency
from .serializers import FuelEffeciencySerializer


class FuelEffeciencyViewSet(viewsets.ModelViewSet):
    serializer_class = FuelEffeciencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    renderer_classes = (AdminRenderer, XMLRenderer, JSONRenderer, )

    def get_queryset(self):
        return FuelEffeciency.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClassBasedView(generics.ListCreateAPIView):
    serializer_class = FuelEffeciencySerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return FuelEffeciency.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClassBasedDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = FuelEffeciencySerializer

    def get_queryset(self):
        return FuelEffeciency.objects.all()


class BaseView(TemplateView):
    template_name = 'milage/milage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        db_pks = [i.id for i in FuelEffeciency.objects.all()]
        context['db_pk'] = db_pks

        description = ["""This is cooler than it seems.""",
            """<a href=https://en.wikipedia.org/wiki/Representational_state_transfer>Rest frameworks</a> let you push data in and out of an appserver agnostic of the view.  An iPhone app, a Casio watch, and a Playstation4 can send and receive the same data from the server.  This page is just one view of the data, as html, xml, or json.  The display here is just to make it accessible to web browsers.""",
            """The top list and the botton grid just use different wires to connect to the SQL.  I like the bottom grid myself.""",
        ]
        context['description'] = description

        return context
