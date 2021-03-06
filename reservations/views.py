import datetime as dt

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .forms import MakeReservationForm
from .models import Reservation
from .functions import (
    sort_res,
    check_availability,
    send_success_email,
    get_res_month,
) 

def make_res(request):
    user = User.objects.get(id=request.user.id)
    form = MakeReservationForm(instance=user, initial={
                                                        'date':dt.date.today(), 
                                                        'check_in':dt.time(hour=9,minute=0),
                                                        'check_out':dt.time(hour=10,minute=0)
    })

    if request.method == "POST":
        form = MakeReservationForm(request.POST, instance=user)
        if form.is_valid():

            # Form info
            form_date = form.cleaned_data['date']
            form_check_in = form.cleaned_data['check_in']
            form_check_out = form.cleaned_data['check_out']

            # performing extra-verification process: date
            if form_date < dt.date.today():
                messages.error(
                    request, "Ingrese una fecha válida.")
                context = {
                    'form': form,
                }
                return render(request, 'reservations/make.html', context)

            # performing extra-verification process: time
            elif form_check_out < form_check_in or form_check_in < dt.time(hour=9, minute=0) or form_check_out > dt.time(hour=22, minute=0):
                messages.error(
                    request, "Ingrese una hora válida.")
                context = {
                    'form': form,
                }
                return render(request, 'reservations/make.html', context)

            # if inputs are good:
            else:
                # getting reservations by date:
                res_by_date = list(Reservation.objects.filter(date=form_date))

                # reservation requested by user
                actual_reservation = Reservation(owner=user,
                                                 date=form_date,
                                                 check_in=form_check_in,
                                                 check_out=form_check_out)

                # Checking availability
                sorted_reservations = sort_res(res_by_date)
                outcome = check_availability(
                    sorted_reservations, actual_reservation)
                if outcome == 0:
                    actual_reservation.save()
                    send_success_email(user, actual_reservation)
                    return redirect('reservations:success')
                else:
                    messages.error(
                        request, "Alguien ya tomó reservó ese espacio :(")
                    context = {
                        'form': form,
                    }
                    return render(request, 'reservations/make.html', context)

    context = {
        'form': form,
    }
    return render(request, 'reservations/make.html', context)


def reservations_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations':reservations,
        }
    return render(request, 'reservations/list.html', context)


def res_by_date(request):
    pass
# TODO: Hacer res_by_date view


def success(request):
    return render(request, 'reservations/success.html')

@login_required()
def my_res(request):
    user = User.objects.get(id=request.user.id)
    reservations = Reservation.objects.filter(owner=user)
    context = {
        'reservations':reservations,
        }
    return render(request, 'reservations/my_reservations.html', context)


def expired_res(request):
    pass
# TODO: Hacer expired_res view
