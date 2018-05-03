import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_admin(request):
    return HttpResponse('login admin')

def  admin_subir(request):
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        archivo = fs.save(os.path.join('download/',f.name), f)
        return redirect('/')
    return render(request, 'subir.html')
