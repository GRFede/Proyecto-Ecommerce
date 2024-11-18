from django import forms



class CrearUsuario(forms.Form):
    nombres=forms.CharField(max_length=20)
    apellidos=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    foto=forms.ImageField(required=False)


