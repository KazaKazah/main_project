from django.urls import path

from content.views import *

urlpatterns = [
    path('content/', AnimationHomePage.as_view(), name='anima_home')
]
