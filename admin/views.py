import os
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse

from noticias.models import Noticia
from admin.forms import es_valido

ADMIN_URL_SUBIR = '/admin/subir'
ADMIN_URL_LOGIN = '/admin/login'
ADMIN_URL_LOGOUT = '/admin/logout'
ADMIN_URL_CREAR_NOTICIA = '/admin/noticia/crear'

def login_admin(request):
    if request.user.is_superuser:
        return redirect(ADMIN_URL_SUBIR)
    else:
        if request.method == 'POST':
            u = request.POST['admin']
            p = request.POST['password']
            user = authenticate(request, username=u, password=p)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect(ADMIN_URL_SUBIR)
            else:
                return redirect(ADMIN_URL_LOGIN)
        return render(request, 'login_admin.html')

def logout_admin(request):
    if request.user.is_superuser:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse(status=404, content='La pagina que quiere acceder no existe')

def admin_subir(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            f = request.FILES['file']
            fs = FileSystemStorage()
            archivo = fs.save(os.path.join('download/',f.name), f)
            return redirect('/')
        return render(request, 'subir.html')
    else:
        return HttpResponse(status=404, content='La pagina que quiere acceder no existe')

def admin_crear_noticia(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            t = request.POST['titulo']
            d = request.POST['descripcion']
            c = request.POST['contenido']
            if es_valido(t,d,c):
                n = Noticia.objects.create(titulo=t, descripcion=d, text=c)
                return redirect('/')
            else:
                return HttpResponse(status=404, content='Hubo un error')
        return render(request, 'noticia_crear.html')
    else:
        return HttpResponse(status=404, content='La pagina que quiere acceder no existe')
