from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bands.models import Band
from .forms import CreateBandForm


def profile(request):
    user = User.objects.get(id=request.user.id)
    bands = Band.objects.filter(owner=user)

    context = {
        'user' : user,
        'bands': bands,
    }
    return render(request, 'profiles/profile.html', context)


def band_creation(request):
    form = CreateBandForm()
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CreateBandForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('profiles:profile')

    context = {
        'form': form,
    }
    return render(request, 'profiles/create_band.html', context)