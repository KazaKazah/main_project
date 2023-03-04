from django.shortcuts import render
from .models import *
from django.views.generic import *


# Create your views here.

class RHomeView(ListView):
    model = Rrrr
    template_name = 'main/rec/rec_home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RHomeView, self).get_context_data(*args, **kwargs)
        return context


class RDetailView(DetailView):
    model = Rrrr
    slug_field = 'slug'
    template_name = 'main/rec/rec_detail.html'

    def get_context_data(self, **kwargs):
        ret = Ret.objects.filter(rrrr_id=kwargs.get('object').id)
        context = {
            'ret': ret
        }
        return context


class RCDetailView(DetailView):
    model = Ret
    slug_field = 'slug'
    template_name = 'main/rec/rec_detail_charester.html'

    def get_context_data(self, **kwargs):
        typ = Typ.objects.filter(ret_id=kwargs.get('object').id)
        context = {
            'typ': typ
        }
        return context


class RCDDetailView(DetailView):
    model = Typ
    slug_field = 'slug'
    template_name = 'main/rec/rec_charester_detail.html'

    def get_context_data(self, **kwargs):
        tyer = Tyer.objects.filter(typ_id=kwargs.get('object').id)
        context = {
            'tyer': tyer
        }
        return context