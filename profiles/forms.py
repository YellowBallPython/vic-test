from django import forms
from bands.models import Band
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateBandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'img']
        required = []
