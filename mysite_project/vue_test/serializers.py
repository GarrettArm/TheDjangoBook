from rest_framework import serializers
from .models import FuelEffeciency
from django.contrib.auth.models import User


class FuelEffeciencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelEffeciency
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('miles_driven', 'gallons_used', 'date_measured', 'date_recorded', 'owner')


# class UserSerializer(serializers.ModelSerializer):
#     fuelefficiency = serializers.PrimaryKeyRelatedField(many=True, queryset=FuelEffeciency.objects.all())
#     class Meta:
#         model = User 
#         fields = ('id', 'username', 'fuelefficiency')
