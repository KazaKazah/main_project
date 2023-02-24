from django.db import models
from django_s3_storage.storage import S3Storage

from content.models.content.animations.animation import Animation

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')


class CharesterAnima(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='имя персонажа')
    cha_pic = models.ImageField(storage=storage, null=True, blank=True, default='', verbose_name='картинка персонажа')
    animation = models.ForeignKey(Animation, on_delete=models.PROTECT, default='',
                                  verbose_name='к какому аниме принадлежит')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('anima_home')

    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'персонажи'
