from django.views.generic import *

from .models import *


# Create your views here.

class GalHomeView(ListView):
    model = Gallery
    template_name = 'main/gallery/home.html'

