from django import forms



class CrearUsuario(forms.Form):
    nombres=forms.CharField(max_length=20)
    apellidos=forms.CharField(max_length=20)
    nacimiento=forms.DateField(required=False)
    foto=forms.ImageField(required=False)

class CrearProducto(forms.Form):
    nombres_producto=forms.CharField(max_length=20)
    descripcion_breve_producto=forms.CharField(max_length=200)
    descripcion_extendida_producto=forms.CharField(max_length=1000)
    precio=forms.IntegerField()
    imagen_producto=forms.ImageField(required=False)
    categoria_producto=forms.CharField(max_length=20)

class BuscarProducto(forms.Form):
    nombres_producto = forms.CharField(max_length=20, required=False)
    
