from django.views.generic import *

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
