from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Anuncio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Fotos_Anuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', verbose_name='Image')   