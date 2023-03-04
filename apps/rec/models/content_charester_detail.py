from django.db import models
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')
from apps.rec.models.content_charester import Typ


class Tyer(models.Model):
    name = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='имя')
    vselen = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='вселенная')
    age = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='возраст')
    plane = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='родина')
    race = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='раса')
    race_body = models.TextField(default='')
    gender = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='пол')
    #
    h_color = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='цвет волос')
    e_color = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='цвет глаз')
    rost = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='рост')
    ves = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='вес')
    grud = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='грудь')
    tali = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='талия')
    bedr = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='бедра')
    #
    titul = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='титул')
    titul_body = models.TextField(null=True, blank=True, verbose_name='описание титула')
    power = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='сила')
    power_body = models.TextField(default='', null=True, blank=True, verbose_name='описание силы')
    gear = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='снаряжение')
    gear_body = models.TextField(default='', null=True, blank=True, verbose_name='описание снаряжения')
    #
    detail_pic = models.ImageField(storage=storage, null=True, blank=True, verbose_name='картинка')
    #
    familiar = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='фамилияр')
    familiar_body = models.TextField(default='', null=True, blank=True, verbose_name='описание фамилияра')
    whisper = models.CharField(max_length=255, default='', null=True, blank=True, verbose_name='дух')
    whisper_body = models.TextField(default='', null=True, blank=True, verbose_name='описание духа')
    typ = models.ForeignKey(Typ, on_delete=models.PROTECT, default='')
    slug = models.SlugField(unique=True, default='')

    class Meta:
        verbose_name = 'информация о персонаже'
        verbose_name_plural = 'информации о персонажах'

    def __str__(self):
        return self.name
