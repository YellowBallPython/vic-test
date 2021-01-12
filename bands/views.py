from django.shortcuts import render

def create_band(request):
    
    context = {}
    return render(request, 'profile/create_band.html', context)
