from django import forms
from .models import Anuncio
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class AnuncioForm(forms.ModelForm):
    titulo = forms.CharField()
    descripcion = forms.CharField()
 

    class Meta:
        model = Anuncio
        fields = [
            
            'titulo',
            'descripcion'
            
        ]

