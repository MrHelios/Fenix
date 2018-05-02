from django.http import HttpResponse
#from django.shortcuts import render

def juego1_view(request):
    return HttpResponse('Esto es el juego1')


def juego1_download(request):
    return HttpResponse('Aqui podras bajar el juego')
