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


class AnimaAnimationsCreateForm(forms.ModelForm):
    class Meta:
        model = Animation
        fields = ('name', 'body', 'url', 'animations_type', 'anima_pic')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'animations_type': forms.Select(attrs={'class': 'form-control'}),
        }

        

class AnimaCharesterCreateForm(forms.ModelForm):
    class Meta:
        model = CharesterAnima
        fields = ('name', 'url', 'animation', 'cha_pic')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'animation': forms.Select(attrs={'class': 'form-control'}),
        }
