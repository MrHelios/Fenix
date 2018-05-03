import os
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_admin(request):
    if request.method == 'POST':
        u = request.POST['admin']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user is not None and user.is_superuser:
            return redirect('/admin/subir')
        else:
            return redirect('/admin/login')
    return render(request, 'login_admin.html')

def  admin_subir(request):
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        archivo = fs.save(os.path.join('download/',f.name), f)
        return redirect('/')
    return render(request, 'subir.html')
