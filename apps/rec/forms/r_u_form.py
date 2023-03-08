from django import forms

from apps.rec.models import *


class RUForm(forms.ModelForm):
    class Meta:
        model = Rrrr
        fields = ('name', 'title')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
