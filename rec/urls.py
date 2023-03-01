from django.urls import path
from .views import *

urlpatterns = [
    path('content/', RHomeView.as_view(), name='rec_home_pages'),
    path('content/detail/<slug:slug>/', RDetailView.as_view(), name='detail_pages_rec'),
]
