#from django.shortcuts import render
from django.http import HttpResponse

def login_admin(request):
    return HttpResponse('login admin')

def  admin_subir(request):
    return HttpResponse('admin subir')
