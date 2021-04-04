from django.urls import path

from . import views




urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    path('create/', views.anuncio_create, name='create'),
    path('<int:id>', views.anuncio_detail, name='detail' )
    
]