from django.views.generic import * 
from content.models import *


class AnimationHomePage(ListView):
    paginate_by = 3
    model = AnimationsName
    template_name = 'main/content/animations/home_anima.html'

    def get_context_data(self, *args, **kwargs):
        anima = AnimationsName.objects.all()
        context = {
            'anima': anima
        }
        return context
