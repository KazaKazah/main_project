from django.urls import path

from content.views.animated_view import *

urlpatterns = [
    path('content/', AnimationHomeView.as_view(), name='anima_home'),
    path('content/detail/<slug:slug>/', AnimeTypeDetailView.as_view(), name='anima_detail'),
    path('content/detail/<slug:slug>/animations', AnimeAnimaDetailView.as_view(), name='anima_anima_detail'),
]
