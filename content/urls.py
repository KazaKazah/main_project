from django.urls import path

from .views import *

urlpatterns = [
    path('content/', ContentHomeView.as_view(), name='content_home'),
]
