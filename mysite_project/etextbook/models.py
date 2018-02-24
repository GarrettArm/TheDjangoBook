from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:20] or self.id

    def help_text(self):
        return """each uploaded files is saved at /var/www/django/media/ and is accessible through the admin panel"""
