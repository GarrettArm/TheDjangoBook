from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description_or_none', 'document', 'uploaded_at')
    readonly_fields = ('help_text', 'description_or_none', 'uploaded_at',)

    def help_text(self, instance):
        return instance.help_text()

    def description_or_none(self, instance):
        return instance.description or 'No Description Provided'

    def show_url(self, instance):
        url = reverse('document', kwargs={'pk': instance.pk})
        response = format_html("""<a href="{}">{}</a>""", url, url)
        return response

admin.site.register(Document, DocumentAdmin)
