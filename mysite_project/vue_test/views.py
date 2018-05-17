import datetime

from django.views.generic import TemplateView
from rest_framework import viewsets, generics
from .models import FuelEffeciency
from .serializers import FuelEffeciencySerializer
# from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response


class FuelEffeciencyViewSet(viewsets.ModelViewSet):
    queryset = FuelEffeciency.objects.all()
    serializer_class = FuelEffeciencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


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


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class TestView(TemplateView):
    template_name = 'vue_test/vue_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['current_datestuff'] = current_time
        counters = [1, 2, 3, 4]
        context['counters'] = counters
        db_pks = [i.id for i in FuelEffeciency.objects.all()]
        print(db_pks)
        context['db_pk'] = db_pks
        return context
