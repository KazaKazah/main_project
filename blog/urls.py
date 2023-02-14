from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='detail_page'),
]