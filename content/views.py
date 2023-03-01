from django.views.generic import *

from .models import *


# Create your views here.

class ContentHomeView(ListView):
    model = Contentyp
    template_name = 'main/content/home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContentHomeView, self).get_context_data(*args, **kwargs)
        return context


class ContentDetailView(DetailView):
    model = Contentyp
    slug_field = 'url'
    template_name = 'main/content/detail_page.html'

    def get_context_data(self, *args, **kwargs):
        cont = Content.objects.filter(=kwargs.get('object').id)
        context = {
            'cont': cont
        }
        return context
