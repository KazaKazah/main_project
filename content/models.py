from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


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
        return reverse('content_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'вид контента'
        verbose_name_plural = 'виды контента'


class Content(models.Model):
    """контент"""
    name = models.CharField(max_length=255, default='', verbose_name='название контента')
    cont_pic = models.ImageField(storage=storage, blank=True, null=True, default='', verbose_name='картинка контента')
    tit = models.CharField(max_length=100, default='', verbose_name='краткое описание контента')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'контенты'
