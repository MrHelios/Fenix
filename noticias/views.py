from django.http import Http404
from django.shortcuts import render

from noticias.models import Noticia

def ultimasNoticias(request):
    n = Noticia.objects.all()
    return render(request, 'ultimas_noticias.html', {'noticia': n})

def noticiaPorId(request, num):
    try:
        n = Noticia.objects.get(pk=num)
    except Noticia.DoesNotExist:
        raise Http404('La noticia que quiere acceder no existe')
    return render(request, 'noticia_id.html', {'noti': n})
