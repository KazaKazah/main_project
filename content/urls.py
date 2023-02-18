from django.urls import path

from content.views.animated_view import *

urlpatterns = [
    path('content/', AnimationHomeView.as_view(), name='anima_home'),
    path('content/detail/<int:pk>/', AnimeTypeDetailView.as_view(), name='anima_detail'),
]
