from django.views.generic import *

from apps.rec.models import *


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
