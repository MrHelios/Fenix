from django.contrib import admin
from django.urls import path, include

from sitio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('', include('noticias.urls')),

    path('u/', include('usuarios.urls')),

    path('g/', include('juegos.urls')),
]
