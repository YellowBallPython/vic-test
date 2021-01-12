from django import forms
from .models import Band

class CreateBandForm(forms.ModelForm):
    model = Band
    fields = ['name', 'genre', 'img']