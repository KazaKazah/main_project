from django.views.generic import *
from content.forms import *
from content.models import *


class AnimeCreateTypeView(CreateView):
    model = AnimationsType
    form_class = AnimaTypeCreateForm
    template_name = 'main/content/animations/create/anima_type_create.html'
