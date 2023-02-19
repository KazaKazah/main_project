from django.views.generic import *

from content.models import *


class AnimeAnimaDetailView(DetailView):
    model = AnimationsType
    slug_field = 'url'
    template_name = 'main/content/animations/detail/detail_anima_anima.html'

    def get_context_data(self, *args, **kwargs):
        animas = Animation.objects.filter(animations_type_id=kwargs.get('object').id)
        context = {
            'animas': animas
        }
        return context
