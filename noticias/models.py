from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    fecha = models.DateField(auto_now = True)

    def __str__(self):
        return self.titulo
