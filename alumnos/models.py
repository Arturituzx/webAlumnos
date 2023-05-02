from django.db import models

# Create your models here.

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    telefono = models.CharField(verbose_name='Telefono', max_length=9)

    def __str__(self):
        fila = 'Nombre:'+ self.nombre + '\n' + 'Telefono:'+ self.telefono + '\n' + 'Imagen:'+ self.imagen 
        return fila
