from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='test-buckets-ny')

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=500, default='', verbose_name='название')
    body = models.TextField(default='', verbose_name='описание')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    author = models.ForeignKey(User, on_delete=models.PROTECT, default='', verbose_name='автор')
    post_pic = models.ImageField(storage=storage, null=True, blank=True, default='',
                                 verbose_name='картинка поста')
    url = models.SlugField(unique=True, max_length=100, default='')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_page', kwargs={'slug': self.url})
