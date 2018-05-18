import datetime

from django.views.generic import TemplateView
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework_xml.renderers import XMLRenderer

from .models import FuelEffeciency
from .serializers import FuelEffeciencySerializer


class FuelEffeciencyViewSet(viewsets.ModelViewSet):
    queryset = FuelEffeciency.objects.all()
    serializer_class = FuelEffeciencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    renderer_classes = (AdminRenderer, XMLRenderer, JSONRenderer, )


class ClassBasedView(generics.ListCreateAPIView):
    queryset = FuelEffeciency.objects.all()
    serializer_class = FuelEffeciencySerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ClassBasedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelEffeciency.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = FuelEffeciencySerializer


class BaseVueView(TemplateView):
    template_name = 'vue_test/vue_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        db_pks = [i.id for i in FuelEffeciency.objects.all()]
        context['db_pk'] = db_pks
        return context
