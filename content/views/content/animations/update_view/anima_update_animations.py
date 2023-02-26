from django.views.generic import *
from content.forms import *
from content.models import *


class AnimeUpdateAnimationsView(UpdateView):
    model = Animation
    form_class = AnimaAnimationsUpdateForm
    template_name = 'main/content/animations/update/anima_animations_update.html'