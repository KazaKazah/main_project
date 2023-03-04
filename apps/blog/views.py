from django.urls import reverse_lazy
from django.views.generic import *

from .forms import *
from .models import *


# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'main/blog/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    slug_field = 'url'
    template_name = 'main/blog/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "main/blog/add.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'main/blog/update.html'
    form_class = EditForm

    def get_context_data(self, *args, **kwargs):
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main/blog/delete.html'
    success_url = reverse_lazy('home_page')
