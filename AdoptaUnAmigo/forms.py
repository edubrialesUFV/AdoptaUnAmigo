from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    titulo = forms.CharField()
    descripcion = forms.CharField()
 

    class Meta:
        model = Anuncio
        fields = [
            
            'titulo',
            'descripcion'
            
        ]

