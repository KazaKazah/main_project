from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import *

class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'body', 'post_pic', 'author', 'url')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'body': SummernoteWidget(),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'body', 'post_pic', 'url']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'body': SummernoteWidget(),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }