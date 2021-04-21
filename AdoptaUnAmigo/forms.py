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
            'animal',
            'raza',
            'sexo',
            'edad',
            'descripcion'
            
        ]

class Fotos_AnuncioForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta(AnuncioForm.Meta):
        fields = AnuncioForm.Meta.fields + ['images',]


class ContactoForm(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea, required=True)