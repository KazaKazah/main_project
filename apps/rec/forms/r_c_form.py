from django import forms

from apps.rec.models import *


class RCForm(forms.ModelForm):
    class Meta:
        model = Ret
        fields = ('name', 'title_con', 'slug', 'cont_pic')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title_con': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
