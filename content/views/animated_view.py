from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import *

from content.models import *


class AnimationHomePage(ListView):
    model = Animations
    template_name = 'main/content/animations/home_anima.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        anima = Animations.objects.all()
        context = {
            'anima': anima
        }
        return context


def animations_list(request):
    object_list = Animations.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        animations = paginator.page(page)
    except PageNotAnInteger:
        animations = paginator.page(1)
    except EmptyPage:
        animations = paginator.page(paginator.num_pages)
    return render(request, 'main/content/animations/home_anima.html', {'page': page, 'animations': animations})
