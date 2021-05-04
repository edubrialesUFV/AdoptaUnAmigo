from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ANIMAL_CHOICES= (
    ('perro','PERRO'),
    ('gato', 'GATO'),
)

SEXO_CHOICES= (
    ('macho','MACHO'),
    ('hembra', 'HEMBRA'),
)
class Anuncio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    animal = models.CharField(max_length=6, choices=ANIMAL_CHOICES, default='perro')
    raza = models.CharField(max_length=20, default='.')
    sexo = models.CharField(max_length=6, choices=SEXO_CHOICES, default='macho')
    edad = models.PositiveIntegerField(default=1)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.titulo
class Fotos_Anuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True, blank=True, default='media/Doggo-1.png')   

class Anuncios_fav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=True)

class MoreinfoUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    foto_perfil = models.ImageField(upload_to='images/', verbose_name='Image', null=True, blank=True, default='images/Sin-foto-de-perfil-en-Facebook.jpg')
    protectora = models.BooleanField(default=False)  
    biografia = models.TextField(null=True, blank=True)
    calle = models.CharField(null=True, blank=True, max_length=50)
    ciudad = models.CharField(null=True, blank=True, max_length=50)