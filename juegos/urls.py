from django.urls import path

from juegos import views

urlpatterns = [
    path('juego1', views.juego1_view),
]
