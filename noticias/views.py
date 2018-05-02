#from django.shortcuts import render
from django.http import HttpResponse

def ultimasNoticias(request):
    return HttpResponse('ultimas noticias')

def noticiaPorId(request, num):
    return HttpResponse(str(num))
