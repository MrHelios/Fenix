from django.urls import path

from juegos import views

urlpatterns = [
    path('juego1', views.juego1_view),
    path('juego1/download', views.juego1_download),
]
