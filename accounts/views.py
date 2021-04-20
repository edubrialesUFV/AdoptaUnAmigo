from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, authenticate, login
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
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    return render(response, 'signup.html', {'form': form})
