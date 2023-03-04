from django.views.generic import *

from apps.rec.models import *


class RHomeView(ListView):
    model = Rrrr
    template_name = 'main/rec/rec_home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RHomeView, self).get_context_data(*args, **kwargs)
        return context