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
