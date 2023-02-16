from django.db import models
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


# Create your models here.


class AnimationsName(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='название анимации')
    title = models.CharField(max_length=255, default='', verbose_name='краткое описание')
    animat_pic = models.ImageField(storage=storage, blank=True, null=True, verbose_name='картника')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'анимационное'
        verbose_name_plural = 'анимациоенное'
