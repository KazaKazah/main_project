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


class AnimeTypeDetailView(DetailView):
    model = Animations
    slug_field = 'url'
    template_name = 'main/content/animations/detail_anima_type.html'

    def get_context_data(self, *args, **kwargs):
        types = AnimationsType.objects.filter(animations_id=kwargs.get('object').id)
        context = {
            'types': types
        }
        return context


class AnimeAnimaDetailView(DetailView):
    model = AnimationsType
    slug_field = 'url'
    template_name = 'main/content/animations/detail_anima_anima.html'

    def get_context_data(self, *args, **kwargs):
        animas = Animation.objects.filter(animations_type_id=kwargs.get('objec').id)
        context = {
            'animas': animas
        }
        return context
