#from django.shortcuts import render
from django.http import HttpResponse

def loginUsuario(request):
    return HttpResponse('login')

def registrarUsuario(request):
    return HttpResponse('registrar')

def configuracionUsuario(request):
    return HttpResponse('configuracion')
