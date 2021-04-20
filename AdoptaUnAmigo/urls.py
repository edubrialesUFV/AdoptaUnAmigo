from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    path('create/', views.anuncio_create, name='create'),
    path('<int:id>', views.anuncio_detail, name='detail' ),
    path('fotos/<int:id>', views.anuncio_images, name='images')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)