from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
# Create your views here.

def register(response):    
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    return render(response, 'signup.html', {'form': form})
