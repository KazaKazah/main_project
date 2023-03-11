from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('summernote/', include("django_summernote.urls")),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('', include('apps.blog.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.rec.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)