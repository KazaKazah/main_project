from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.


class Rrrr(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название')
    title = models.CharField(max_length=200, default='', verbose_name='краткое описание')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'вид контент'
        verbose_name_plural = 'виды контентов'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_pages_rec', kwargs={'slug': self.slug})


class Ret(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название контента')
    title_con = models.CharField(max_length=255, default='', verbose_name='краткое описание контента')
    cont_pic = models.ImageField(upload_to='rrr/', blank=True, null=True, default='')
    rrrr = models.ForeignKey(Rrrr, on_delete=models.PROTECT, default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'название контента'
        verbose_name_plural='названия контентов'

    def __str__(self):
        return self.name

