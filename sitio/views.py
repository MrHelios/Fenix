from django.shortcuts import render

from noticias.models import Noticia

def home(request):
    if Noticia.objects.count() != 0:
        n = Noticia.objects.all()
    else:
        n = []
    return render(request, 'home.html', {'noticia': n})
