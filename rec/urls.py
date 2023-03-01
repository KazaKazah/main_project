from django.urls import path
from .views import *

urlpatterns = [
    path('', RHomeView.as_view(), name='rec_home_page'),
    path('detail/<slug:slug>/', RDetailView.as_view(), name='detail_page_rec'),
]
