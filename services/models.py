from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    subtitle=models.CharField(max_length=100, verbose_name="Subtitulo")
    image=models.ImageField(verbose_name="imagen", upload_to="Services")
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
        ordering=["-created"]

    def __str__(self):
        return self.title





