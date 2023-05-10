from django.db import models

# Create your models here.

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    codAlumno = models.CharField(max_length=8, verbose_name='Codigo de Alumno')
    nombres = models.CharField(max_length=100, verbose_name='Nombre')
    Apellido = models.CharField(max_length=100, verbose_name='Apellido')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    def __str__(self):
        fila = "Nombre: " + self.nombres + " - " + " Apellido: " + self.Apellido
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

   