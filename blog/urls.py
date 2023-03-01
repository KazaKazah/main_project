from django.urls import path

from .views import *


urlpatterns = [
    path('blog/', HomePageView.as_view(), name='home_page_blog'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='detail_page'),
    path('add_post/', PostCreateView.as_view(), name='creat_post_page'),
    path('blog/edit/<int:pk>/', PostUpdateView.as_view(), name='update_post_page'),
    path('blog/<int:pk>/remover/', PostDeleteView.as_view(), name='delete_post_page'),
]