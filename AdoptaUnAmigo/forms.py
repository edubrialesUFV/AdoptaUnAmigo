from django import forms
from .models import Anuncio, Fotos_Anuncio
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

class Fotos_AnuncioForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Fotos_Anuncio
        fields = [
            'image'
        ]