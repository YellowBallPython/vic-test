from django import forms
from bands.models import Band

class CreateBandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'img']