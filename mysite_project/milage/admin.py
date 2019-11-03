from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import FuelEffeciency


class FuelEffeciencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "miles_driven",
        "gallons_used",
        "date_measured",
        "date_recorded",
        "owner",
    )


admin.site.register(FuelEffeciency, FuelEffeciencyAdmin)
