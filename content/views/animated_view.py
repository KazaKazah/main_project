from django.views.generic import *

from content.models import *


class AnimationHomePage(ListView):
    model = AnimationsName
    template_name = 'main/content/animations/home_anima.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        anima = AnimationsName.objects.all()
        context = {
            'anima': anima
        }
        return context
