from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
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
def anuncio_create(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            anuncio_nuevo= form.save(commit=False)
            anuncio_nuevo.user = request.user
            anuncio_nuevo.save()
            return HttpResponseRedirect(reverse('home'))
            
    else:
        form = AnuncioForm()  
    context = {
        'form': form
    }
    return render(request, 'anuncio_create.html', context)

@login_required(login_url='login')
def anuncio_detail(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    context = {'anuncio': anuncio}
    return render(request, 'anuncio_detail.html', context)


def ajustes(request):
    return render(request, 'Perfil/ajustes.html')

def perfil(request):
    return render(request, 'Perfil/perfil.html')