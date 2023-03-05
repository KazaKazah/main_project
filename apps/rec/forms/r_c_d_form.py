from django import forms

from apps.rec.models import *


class RCDForm(forms.ModelForm):
    class Meta:
        model = Typ
        fields = ('name', 'slug', 'typ_pic', 'ret')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'ret': forms.Select(attrs={'class': 'form-control'}),
        }
