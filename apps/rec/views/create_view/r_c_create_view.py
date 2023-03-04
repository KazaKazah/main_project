from django.views.generic import *

from apps.rec.forms import *
from apps.rec.models import *


class RCCreateView(CreateView):
    model = Ret
    form_class = RCForm
    template_name = 'main/rec/create/rec_create_charester.html'
