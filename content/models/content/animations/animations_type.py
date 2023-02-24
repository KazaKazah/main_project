from django.db import models
from django.urls import reverse
from content.models.content.animations.animations import Animations
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


class AnimationsType(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название жанра')
    body = models.TextField(default='', verbose_name='краткое описание жанра')
    animations = models.ForeignKey(Animations, on_delete=models.PROTECT, default='',
                                   verbose_name='к какой категории относиться')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anima_anima_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
