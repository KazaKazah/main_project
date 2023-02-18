from django.urls import path

from content.views.animated_view import AnimationHomePage

urlpatterns = [
    path('content/', AnimationHomePage.as_view(), name='anima_home')
]
