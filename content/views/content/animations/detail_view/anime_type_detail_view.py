from django.views.generic import *

from content.models import *


class AnimeTypeDetailView(DetailView):
    model = Animations
    slug_field = 'url'
    template_name = 'main/content/animations/detail/detail_anima_type.html'

    def get_context_data(self, *args, **kwargs):
        types = AnimationsType.objects.filter(animations_id=kwargs.get('object').id)
        context = {
            'types': types
        }
        return context
