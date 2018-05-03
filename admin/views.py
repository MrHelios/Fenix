import os
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse

ADMIN_URL_SUBIR = '/admin/subir'
ADMIN_URL_LOGIN = '/admin/login'
ADMIN_URL_LOGOUT = '/admin/logout'

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
