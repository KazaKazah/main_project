from django.views.generic import *
from content.forms import *
from content.models import *


class AnimeCreateAnimationsView(CreateView):
    model = Animation
    form_class = AnimaAnimationsCreateForm
    template_name = 'main/content/animations/create/anima_animations_create.html'