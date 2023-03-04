from django.db import models
from django.shortcuts import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')
from apps.rec.models.content_name import Ret

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
