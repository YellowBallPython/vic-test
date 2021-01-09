from django import forms
from .models import Reservation


class MakeReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'check_in', 'check_out']
