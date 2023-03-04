from django.views.generic import *
from apps.rec.forms import *
from apps.rec.models import *


class RCreateView(CreateView):
    model = Rrrr
    form_class = RForm
    template_name = 'main/rec/create/rec_create.html'
