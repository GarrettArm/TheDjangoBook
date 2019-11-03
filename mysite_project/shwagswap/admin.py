from django.contrib import admin
from .models import Shwag, ShwagType, Transaction


class ShwagAdmin(admin.ModelAdmin):
    list_display = ("name", "item_type", "photo_site", "creation_time")


class ShwagTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("creator", "have_count", "have_item", "wanted_count", "wanted_item")


admin.site.register(Shwag, ShwagAdmin)
admin.site.register(ShwagType, ShwagTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
