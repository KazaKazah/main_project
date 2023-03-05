from django.views.generic import *

from apps.rec.forms import *
from apps.rec.models import *


class RCDCreateView(CreateView):
    model = Typ
    form_class = RCDForm
    template_name = 'main/rec/create/rec_charester_create.html'
