from django.contrib import admin
from .models import Anuncio, Fotos_Anuncio, Anuncios_fav, MoreinfoUsers
# Register your models here.
admin.site.register(Anuncio)
admin.site.register(Fotos_Anuncio)
admin.site.register(Anuncios_fav)
admin.site.register(MoreinfoUsers)