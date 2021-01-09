import datetime as dt

from .models import Reservation
from django.contrib.auth.models import User

"""
File de funciones para el views de Reservations
"""

# Ordena una lista las reservas de menor a mayor
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

# Chequea si la reservación cabe en el sistema


def check_availability(sorted_list, reservation):
    opening = dt.time(hour=9, minute=0)
    closing = dt.time(hour=21, minute=0)
    midnight_open = dt.time(hour=0, minute=0, second=1)
    midnight_close = dt.time(hour=11, minute=59, second=59, microsecond=59)
    sorted_list.insert(0, Reservation(
        owner=dummy_user, check_in=midnight_open, check_out=opening))
    sorted_list.append(Reservation(
        owner=dummy_user, check_in=closing, check_out=midnight_close))
    for i in range(1, len(sorted_list)):
        print(f"Espacio {i} en {type(sorted_list)}")
        if sorted_list[i-1].check_out <= reservation.check_in and reservation.check_out <= sorted_list[i].check_in:
            return 0
    return 1
