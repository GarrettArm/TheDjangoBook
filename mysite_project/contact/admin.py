from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('creation_time', 'subject', 'email', 'message')


admin.site.register(Comment, CommentAdmin)
