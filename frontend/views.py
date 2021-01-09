from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def contact(request):
    pass
# TODO: Hacer front:contact view
