from django.db import models


class FuelEffeciency(models.Model):
    miles_driven = models.DecimalField(decimal_places=2, max_digits=6)
    gallons_used = models.DecimalField(decimal_places=3, max_digits=6)
    date_measured = models.DateField()
    date_recorded = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='fuelefficiency', on_delete=models.CASCADE)
