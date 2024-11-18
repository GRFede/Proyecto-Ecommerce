from django.db import models

# Create your models here.

class Personas(models.Model):
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    edad=models.IntegerField()
    foto=models.ImageField(upload_to='imagenes-usuario', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombres}{self.apellidos}{self.edad}{self.foto}'

