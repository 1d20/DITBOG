from django import forms
from django.forms import ModelForm
from models import Description


class DescriptionForm(ModelForm):
    class Meta:
        model=Description
        fields = ['title', 'keywords', 'features', 'short_description', 'full_description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'features': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '45'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '45'}),
            'full_description': forms.Textarea(attrs={'class': 'form-control', 'rows': '7', 'cols': '45'}),
        }