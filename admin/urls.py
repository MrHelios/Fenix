from django.urls import path

from admin import views

urlpatterns = [
    path('login', views.login_admin),
    path('subir', views.admin_subir),
]
