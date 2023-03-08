from django.views.generic import *

from .models import *


# Create your views here.


class AlbumHomeView(ListView):
    model = Album
    template_name = 'main/gallery/gallery_home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumHomeView, self).get_context_data(*args, **kwargs)
        return context
