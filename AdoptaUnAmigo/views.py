from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Anuncio, Fotos_Anuncio, Anuncios_fav
from django.contrib.auth.decorators import login_required
from .forms import AnuncioForm, Fotos_AnuncioForm, ContactoForm
from django.forms import modelformset_factory
from django.conf import settings
from django.core.mail import send_mail

@login_required(login_url="login")
def index(request):
    context = {}
    search = request.GET.get('search')
    if search:
        anuncios = Anuncio.objects.filter(
            titulo__icontains=search) | Anuncio.objects.filter(
                raza__icontains=search) | Anuncio.objects.filter(
                    animal__icontains=search) | Anuncio.objects.filter(
                        sexo__icontains=search) | Anuncio.objects.filter(
                            descripcion__icontains=search)
        if anuncios:
            fotos_total=[]
            for anuncio in anuncios:
                fotos_total.append(Fotos_Anuncio.objects.filter(anuncio=anuncio).first())
            context['page'] = 'index_search'
        else:
            fotos_total=Fotos_Anuncio.objects.all()
            context['page'] = 'index'
    else:
        fotos_total=Fotos_Anuncio.objects.all()
        context['page'] = 'index'
    fotos_guardadas=[]
    temp=0
    for foto in fotos_total:
        if temp == foto.anuncio:
            temp=foto.anuncio
            continue

        else:
            fotos_guardadas.append(foto)
            temp=foto.anuncio
    anuncio_fav = request.GET.get('id_anunciofav')
    print()
    print(anuncio_fav)
    if anuncio_fav:
        anuncio_fav_nuevo= Anuncios_fav.objects.filter(anuncio=anuncio_fav)
        if anuncio_fav_nuevo:
            anuncio_fav_nuevo.delete()
        else:
            anuncio_fav = get_object_or_404(Anuncio, pk=anuncio_fav)
            Anuncios_fav.objects.create(user=request.user, anuncio=anuncio_fav)
        
    context['fotos'] = fotos_guardadas
    return render(request, "home.html", context)

@login_required(login_url="login")
def like(request):
    anuncios=Anuncios_fav.objects.all()
    fotos_total=[]
    for anuncio in anuncios:
        foto_like=Fotos_Anuncio.objects.filter(anuncio=anuncio.anuncio).first()
        fotos_total.append(foto_like)
    fotos_guardadas=[]
    print(fotos_total)
    temp=0
    for foto in fotos_total:
        if temp == foto.anuncio:
            temp=foto.anuncio
            print(temp)
            continue

        else:
            fotos_guardadas.append(foto)
            temp=foto.anuncio
        
    context={'fotos': fotos_guardadas, 'page':'like'}
    return render(request, "anuncio_like.html", context)

@login_required(login_url="login")
def anuncio_create(request):
    if request.method == 'POST':
        form = Fotos_AnuncioForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            titulo = form.cleaned_data['titulo']
            animal = form.cleaned_data['animal']
            raza = form.cleaned_data['raza']
            sexo = form.cleaned_data['sexo']
            edad = form.cleaned_data['edad']
            descripcion = form.cleaned_data['descripcion']
            anuncio_nuevo = Anuncio.objects.create(user=user, titulo=titulo, animal=animal, raza=raza, sexo=sexo, descripcion=descripcion, edad=edad)
            for f in files:
                Fotos_Anuncio.objects.create(anuncio=anuncio_nuevo, image=f)
   
        return HttpResponseRedirect('/')
    return render(request, 'anuncio_create.html')

@login_required(login_url='login')
def anuncio_detail(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    print(anuncio.user.email)
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data['mensaje']
            mensaje = f'El usuario "{request.user}" te ha mandado un mensaje preguntando por tu anuncio: {anuncio.titulo} \n------------------\n' + mensaje
            email_from = settings.EMAIL_HOST_USER
            try:
                send_mail(f'{request.user} te ha mandado un mensaje', mensaje, email_from, [anuncio.user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    context = {'anuncio': anuncio, 'form': form}
    return render(request, 'anuncio_detail.html', context)

@login_required(login_url='login')
def ajustes(request):
    return render(request, 'Perfil/ajustes.html')
    
@login_required(login_url='login')
def perfil(request):
    anuncios=Anuncio.objects.filter(user=request.user)
    fotos_total=[]
    for anuncio in anuncios:
        foto_like=Fotos_Anuncio.objects.filter(anuncio=anuncio).first()
        fotos_total.append(foto_like)
    delete = request.GET.get('delete')
    if delete:
        anuncio_delete = Anuncio.objects.get(id=delete)
        anuncio_delete.delete()
        return HttpResponseRedirect('/')
    print(fotos_total)
   
    context={'fotos': fotos_total}
    return render(request, 'Perfil/perfil.html', context)

@login_required(login_url='login')
def editar_perfil(request):
    return render(request, 'Perfil/editar.html')