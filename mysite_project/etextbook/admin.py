from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('description', 'document', 'uploaded_at')


admin.site.register(Document, DocumentAdmin)
