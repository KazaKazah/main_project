from django.views.generic import *

from apps.rec.models import *


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
