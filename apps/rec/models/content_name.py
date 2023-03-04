from django.db import models
from django.shortcuts import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')
from apps.rec.models.content_type import Rrrr


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
