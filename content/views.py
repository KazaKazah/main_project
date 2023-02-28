from django.views.generic import *

from .models import *


# Create your views here.

class ContentHomeView(ListView):
    model = ContentType
    template_name = 'main/content/home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContentHomeView, self).get_context_data(*args, **kwargs)
        return context


class ContentDetailView(DetailView):
    model = ContentType
    slug_field = 'url'
    template_name = 'main/content/detail_page.html'

    def get_context_data(self, *args, **kwargs):
        cont = Content.objects.filter(content_type_id=kwargs.get('object').id)
        context = {
            'cont': cont
        }
        return context
