from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bands.models import Band
from .forms import CreateBandForm, UserRegisterForm

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}! :)')
            return redirect('frontend:login')

    context = {
        'form':form
    }
    return render(request, 'profiles/register.html', context)

def profile(request):
    user = User.objects.get(id=request.user.id)
    bands = Band.objects.filter(owner=user)

    context = {
        'user' : user,
        'bands': bands,
    }
    return render(request, 'profiles/profile.html', context)

def band_list(request):
    user = User.objects.get(id=request.user.id)
    bands = Band.objects.filter(owner=user)

    context = {
        'bands': bands,
    }
    return render(request, 'profiles/bands.html', context)
    

def band_creation(request):


    form = CreateBandForm()
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CreateBandForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            newband = Band(name=cd['name'], genre=cd['genre'], owner=user)
            newband.save()
            return redirect('profiles:profile')

    context = {
        'form': form,
    }
    return render(request, 'profiles/create_band.html', context)

def edit_band(request, id):
    band = Band.objects.get(pk=id)
    form = CreateBandForm(instance=band)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('profiles:profile')
    
    return render(request, 'profiles/edit_band.html', {'form':form})