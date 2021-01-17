from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Reservation(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservation')
    date = models.DateField(verbose_name='fecha')
    check_in = models.TimeField(verbose_name='check in')
    check_out = models.TimeField(verbose_name='check out')

    def __str__(self):
        MONTHS = {
            '1': 'Enero',
            '2': 'Febrero',
            '3': 'Marzo',
            '4': 'Abril',
            '5': 'Mayo',
            '6': 'Junio',
            '7': 'Julio',
            '8': 'Agosto',
            '9': 'Setiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre',
        }
        for k, v in MONTHS.items():
            if self.date.month == int(k):
                return f'Owner: {self.owner} - {MONTHS[k]}/{self.date.day}/{self.date.year} - in: {self.check_in} out: {self.check_out}'

    def by_date(self, date=None):
        return Reservation.objects.filter(date=date)
    
    class Meta:
        ordering = ['date']
