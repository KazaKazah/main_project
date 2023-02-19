from django import forms
from django_summernote import SummernoteWidget, SummernoteInplaceWidget

from content.models import *


class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())


class AnimaTypeCreateForm(forms.ModelForm):
    class Meta:
        model = AnimationsType
        fields = ('name', 'body', 'url', 'animations')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'body': SummernoteWidget(),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'animations': forms.Select(attrs={'class': 'form-control'}),
        }
