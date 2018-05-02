from django.urls import path

from noticias import views

urlpatterns = [
    path('noticias', views.ultimasNoticias),
]
