from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')

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
    cont_pic = models.ImageField(storage=storage, blank=True, null=True, default='')
    rrrr = models.ForeignKey(Rrrr, on_delete=models.PROTECT, default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'название контента'
        verbose_name_plural='названия контентов'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_char_page', kwargs={'slug': self.slug})


class Typ(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='имя персонажа')
    ret = models.ForeignKey(Ret, on_delete=models.PROTECT, default='')
    typ_pic = models.ImageField(storage=storage, null=True, blank=True, default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'персонажи'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail_charester_page', kwargs={'slug': self.slug})


class Tyer(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='имя персонажа')
    typ = models.ForeignKey(Typ, on_delete=models.PROTECT, default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'информация о персонаже'
        verbose_name_plural = 'информации о персонажах'

    def __str__(self):
        return self.name