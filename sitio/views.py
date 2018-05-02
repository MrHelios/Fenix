from django.shortcuts import render

from noticias.models import Noticia

def home(request):    
    n = Noticia.objects.all()
    return render(request, 'home.html', {'noticia': n})
