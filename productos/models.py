from django.db import models

# Create your models here.

class Productos(models.Model):
    nombres_producto=models.CharField(max_length=20)
    descripcion_breve_producto=models.CharField(max_length=200)
    descripcion_extendida_producto=models.CharField(max_length=1000)
    precio=models.IntegerField()
    imagen_producto=models.ImageField(upload_to='imagenes-productos', blank=True, null=True)
    categoria_producto=models.CharField(max_length=20)


    def __str__(self):
        return f'{self.id}{self.nombres_producto}{self.descripcion_breve_producto}{self.descripcion_extendida_producto}{self.precio}{self.imagen_producto}{self.categoria_producto}'


