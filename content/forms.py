from django import forms

from content.models import *


class AnimaTypeCreateForm(forms.ModelForm):
    class Meta:
        model = AnimationsType
        fields = ('name', 'body', 'url', 'animations')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'animations': forms.Select(attrs={'class': 'form-control'}),
        }
