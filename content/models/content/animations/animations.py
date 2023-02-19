from django.db import models
from django.urls import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


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

