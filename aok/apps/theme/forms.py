from django import forms
from django.forms import ModelForm
from models import Description


class DescriptionForm(ModelForm):
    class Meta:
        model=Description
        fields = ['title', 'keywords', 'feathures']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'feathures': forms.Textarea(attrs={'class': 'form-control'}),
        }