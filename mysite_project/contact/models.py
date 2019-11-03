from django.db import models


class Comment(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["creation_time"]
