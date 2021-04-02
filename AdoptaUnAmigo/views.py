from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Anuncio
from .forms import AnuncioForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def index(request):
    anuncios=Anuncio.objects.all()
    context={
        'anuncios_todos': anuncios
    }
    return render(request, "home.html", context)


@login_required(login_url="login")
def crear_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            anuncio_nuevo= form.save(commit=False)
            anuncio_nuevo.user = request.user
            anuncio_nuevo.save()
            
            
    else:
        form = AnuncioForm()  
    context = {
        'form': form
    }
    return render(request, 'addAnuncio.html', context)