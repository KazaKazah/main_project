from django.db import models


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название галлереи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'галлерея'
        verbose_name_plural = 'галлерии'
