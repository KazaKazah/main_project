from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название альбома')
    ttt = models.ForeignKey(User, on_delete=models.PROTECT, default='')

    class Meta:
        verbose_name = 'название альбома'
        verbose_name_plural = 'название альбомов'

    def __str__(self):
        return self.name
