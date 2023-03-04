from django.urls import path

from apps.rec.views import *

urlpatterns = [
    path('content/', RHomeView.as_view(), name='rec_home_pages'),
    # ------------------------------------------------------------------------------------------------------------
    path('content/detail/<slug:slug>/', RDetailView.as_view(), name='detail_pages_rec'),
    path('detail/charester/<slug:slug>/', RCDetailView.as_view(), name='detail_char_page'),
    path('detail/charester_detail/<slug:slug>', RCDDetailView.as_view(), name='detail_charester_page'),
    # ------------------------------------------------------------------------------------------------------------
    path('add/content_type', RCreateView.as_view(), name='create_content_type'),
    path('add/content_name', RCCreateView.as_view(), name='create_content_name'),
]
