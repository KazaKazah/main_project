from django.db import models
from django.urls import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


# Create your models here.


class Animations(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название анимации')
    body = models.TextField(default='', verbose_name='краткое описание')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anima_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'вид мультипликации'
        verbose_name_plural = 'виды мультипликации'


class AnimationsType(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название жанра')
    body = models.TextField(default='', verbose_name='краткое описание жанра')
    animations = models.ForeignKey(Animations, on_delete=models.PROTECT, default='',
                                   verbose_name='к какой мультипликации относиться')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anima_anima_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Animation(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название анимации')
    body = models.TextField(default='', verbose_name='краткое описание анимации')
    animations_type = models.ForeignKey(AnimationsType, on_delete=models.PROTECT, default='',
                                   verbose_name='к какому жанру относиться')
    anima_pic = models.ImageField(storage=storage, blank=True, null=True, default='', verbose_name='картинка анимации')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'анимация'
        verbose_name_plural = 'анимации'