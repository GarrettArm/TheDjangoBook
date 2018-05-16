from rest_framework import serializers
from .models import FuelEffeciency

class FuelEffeciencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelEffeciency
        fields = ('miles_driven', 'gallons_used', 'date_measured', 'date_recorded')
