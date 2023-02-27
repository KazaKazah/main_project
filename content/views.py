from django.views.generic import *

from .models import *


# Create your views here.

class ContentHomeView(ListView):
    model = ContentType
    template_name = 'main/content/home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContentHomeView, self).get_context_data(*args, **kwargs)
        return context