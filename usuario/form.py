from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CrearUsuario(UserCreationForm):
    nombres=forms.CharField(max_length=20)
    apellidos=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    foto=forms.ImageField(required=False)
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'nombres', 'apellidos', 'edad', 'foto', 'email', 'password1', 'password2']
        help_texts= {key: '' for key in fields}
