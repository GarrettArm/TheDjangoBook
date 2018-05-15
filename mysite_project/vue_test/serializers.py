from rest_framework import serializers
from .models import FuelEffeciency

class FuelEffeciencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelEffeciency
        fields = '__all__'
