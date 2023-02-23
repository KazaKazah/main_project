from django.urls import path

from content.views import *

urlpatterns = [
    path('content/', AnimationHomeView.as_view(), name='anima_home'),
    # -----------------------------------------------------------------
    path('content/detail/<slug:slug>/', AnimeTypeDetailView.as_view(), name='anima_detail'),
    path('content/detail/<slug:slug>/animations', AnimeAnimaDetailView.as_view(), name='anima_anima_detail'),
    path('content/detail/<slug:slug>/charester', AnimaCharesterDetailView.as_view(), name='anima_charester_detail'),
    # -----------------------------------------------------------------
    path('content/add_type', AnimeCreateTypeView.as_view(), name='anima_type_add'),
    path('content/add_animations', AnimeCreateAnimationsView.as_view(), name='anima_animations_add'),
]
