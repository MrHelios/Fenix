from django.urls import path

from usuarios import views

urlpatterns = [
    path('login', views.loginUsuario),
    path('registrar', views.registrarUsuario),
    path('config', views.configuracionUsuario),
]
