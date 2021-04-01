from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
def index(request):
    context={
    }
    user=request.user
    if user.is_authenticated:
        return render(request, "home.html", context)
    else:
        return redirect("login")


