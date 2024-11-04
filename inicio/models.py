from django.db import models

# Create your models here.

class Personas(models.Model):
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    nacimiento=models.DateField()
    foto=models.ImageField(upload_to='imagenes-usuario', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombres}{self.apellidos}{self.nacimiento}{self.foto}'

class Productos(models.Model):
    nombres_producto=models.CharField(max_length=20)
    descripcion_breve_producto=models.CharField(max_length=200)
    descripcion_extendida_producto=models.CharField(max_length=1000)
    precio=models.IntegerField()
    imagen_producto=models.ImageField(upload_to='imagenes-productos', blank=True, null=True)
    categoria_producto=models.CharField(max_length=20)


    def __str__(self):
        return f'{self.nombres_producto}{self.descripcion_breve_producto}{self.descripcion_extendida_producto}{self.precio}{self.imagen_producto}{self.categoria_producto}'


