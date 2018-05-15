from rest_framework import viewsets
from .models import FuelEffeciency
from .serializers import FuelEffeciencySerializer


class FuelEffeciencyViewSet(viewsets.ModelViewSet):
    queryset = FuelEffeciency.objects.all()
    serializer_class = FuelEffeciencySerializer
