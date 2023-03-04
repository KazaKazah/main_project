from django.views.generic import *

from apps.rec.models import *


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