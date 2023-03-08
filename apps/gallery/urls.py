from django.urls import path

from .views import *

urlpatterns = [
    path('gallery/album', AlbumHomeView.as_view(), name='adlbum_home'),
]
