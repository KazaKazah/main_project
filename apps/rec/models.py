from django.contrib.auth.models import User
from django.db import models
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
        verbose_name_plural = 'названия контентов'

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
