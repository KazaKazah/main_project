from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.


class ContentType(models.Model):
    """виды контента"""
    name = models.CharField(max_length=255, default='', verbose_name='название')
    title = models.CharField(max_length=255, default='', verbose_name='красткое описание')
    ather = models.ForeignKey(User, on_delete=models.PROTECT, default='', verbose_name='автор')
    dates = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'вид контента'
        verbose_name_plural = 'виды контента'
