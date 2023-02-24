from django.views.generic import *
from content.forms import *
from content.models import *

class AnimeCreateCharesterView(CreateView):
    model = CharesterAnima
    template_name = 'main/content/animations/create/anima_charester_create.html'
    form_class = AnimaCharesterCreateForm