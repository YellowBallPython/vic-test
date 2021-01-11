import datetime as dt
from collections import namedtuple

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth.models import User

from .models import Reservation


"""
File de funciones para el views de Reservations
"""

# dummy user para opening y closing
dummy_user = User.objects.get(id=1)

def sort_res(unsorted_list):
    for i in range(1, len(unsorted_list)):
        j = i
        # both values the same
        current_res, temp = unsorted_list[i], unsorted_list[i]
        while unsorted_list[j-1].check_out > current_res.check_in and j > 0:
            # se intercambian lugares
            unsorted_list[j] = unsorted_list[j-1]
            unsorted_list[j-1] = temp
            j -= 1
    return unsorted_list

def check_availability(sorted_list, reservation):
    """
    Genera los constrains 'opening y closing' y compara la reserva entrante
    con las reservas del día.
    """
    opening = dt.time(hour=9, minute=0)
    closing = dt.time(hour=21, minute=0)
    midnight_open = dt.time(hour=0, minute=0, second=1)
    midnight_close = dt.time(hour=11, minute=59, second=59, microsecond=59)
    sorted_list.insert(0, Reservation(
        owner=dummy_user, check_in=midnight_open, check_out=opening))
    sorted_list.append(Reservation(
        owner=dummy_user, check_in=closing, check_out=midnight_close))
    for i in range(1, len(sorted_list)):
        if sorted_list[i-1].check_out <= reservation.check_in and reservation.check_out <= sorted_list[i].check_in:
            return 0
    return 1

def send_success_email(user, reservation):
    # multiple assignment
    subject, from_email, to = 'Thank you ♥', settings.EMAIL_HOST_USER , user.email
    html_content = render_to_string('reservations/success_email.html', {'user':user, 'reservation':reservation})
    send_mail(
    subject,
    '♥',
    from_email,
    [to],
    html_message=html_content,
)

def get_res_month(reservation):

    """
    Regresa el nombre del mes de la reserva.
    """
    MONTHS = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Setiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre',
        }
    month = MONTHS.get(reservation.date.month)
    return month


