from django import forms

from apps.rec.models import *


class RForm(forms.ModelForm):
    class Meta:
        model = Rrrr
        fields = ('name', 'title', 'slug')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
