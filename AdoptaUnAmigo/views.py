from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Anuncio, Fotos_Anuncio
from django.contrib.auth.decorators import login_required
from .forms import AnuncioForm, Fotos_AnuncioForm
from django.forms import modelformset_factory

@login_required(login_url="login")
def index(request):
    anuncios=Anuncio.objects.all()
    fotos=get_object_or_404(Fotos_Anuncio, pk=8)
    context={
        'anuncios_todos': anuncios,
        'fotos': fotos
    }
    return render(request, "home.html", context)


@login_required(login_url="login")
def anuncio_create(request):
    if request.method == 'POST':
        form = Fotos_AnuncioForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            anuncio_nuevo = Anuncio.objects.create(user=user, titulo=titulo, descripcion=descripcion)
            for f in files:
                Fotos_Anuncio.objects.create(anuncio=anuncio_nuevo, image=f)
   
    
    return render(request, 'anuncio_create.html')

@login_required(login_url='login')
def anuncio_detail(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    context = {'anuncio': anuncio}
    return render(request, 'anuncio_detail.html', context)

@login_required(login_url='login')
def ajustes(request):
    return render(request, 'Perfil/ajustes.html')
    
@login_required(login_url='login')
def perfil(request):
    return render(request, 'Perfil/perfil.html')

@login_required(login_url='login')
def editar_perfil(request):
    return render(request, 'Perfil/editar.html')