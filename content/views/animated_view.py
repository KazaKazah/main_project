from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import *

from content.models import *


class AnimationHomePage(ListView):
    model = Animations
    template_name = 'main/content/animations/home_anima.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        anima = Animations.objects.all()
        context = {
            'anima': anima
        }
        return context

