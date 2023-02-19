from django.views.generic import *

from content.models import *


class AnimaCharesterDetailView(DetailView):
    model = Animation
    slug_field = 'url'
    template_name = 'main/content/animations/detail_anima_charester.html'

    def get_context_data(self, *args, **kwargs):
        char = CharesterAnima.objects.filter(animation_id=kwargs.get('object').id)
        context = {
            'char': char
        }
        return context
