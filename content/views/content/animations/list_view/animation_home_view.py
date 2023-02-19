from django.views.generic import *

from content.models import *


class AnimationHomeView(ListView):
    model = Animations
    template_name = 'main/content/animations/home_anima.html'

    def get_context_data(self, *args, **kwargs):
        anima = Animations.objects.all()
        context = {
            'anima': anima
        }
        return context
