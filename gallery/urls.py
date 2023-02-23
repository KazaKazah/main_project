from django.urls import path

from .views import *

urlpatterns = [
    path('gallery/', GalHomeView.as_view(), name='gal_home_page'),
]
