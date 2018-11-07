from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings


class ShwagType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Shwag(models.Model):
    name = models.CharField(max_length=50)
    item_type = models.ForeignKey(ShwagType, on_delete=models.CASCADE)
    photo_site = models.ImageField(upload_to='static/shwag/')
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Transaction(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    have_count = models.PositiveIntegerField()
    have_item = models.ForeignKey(
        Shwag,
        on_delete=models.CASCADE,
        related_name='have_item'
    )
    wanted_count = models.PositiveIntegerField()
    wanted_item = models.ForeignKey(
        Shwag,
        on_delete=models.CASCADE,
        related_name='wanted_item'
    )

    def __str__(self):
        return '{} for {}'.format(self.have_item.name, self.wanted_item.name)

    class Meta:
        ordering = ('have_item', )


