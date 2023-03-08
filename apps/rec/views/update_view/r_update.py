from django.views.generic import *
from apps.rec.forms import *
from apps.rec.models import *


class RUpdateView(UpdateView):
    model = Rrrr
    form_class = RUForm
    template_name = 'main/rec/update/rec_update.html'
