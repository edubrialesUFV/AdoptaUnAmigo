from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def register(response):    
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user=form.save()
            #Login automatico despues de registrarse
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            subject = 'Bienvenido a Adopta Un Amigo'
            message = f'Hola {response.user}!, \nGracias por registrarte en AdoptaUnAmigo.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [response.user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    return render(response, 'signup.html', {'form': form})
