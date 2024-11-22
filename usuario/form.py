from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm


class CrearUsuario(UserCreationForm):
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres=forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos=forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    edad=forms.IntegerField()
    foto=forms.ImageField(required=False)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'nombres', 'apellidos', 'edad', 'foto', 'email', 'password1', 'password2']
        help_texts= {key: '' for key in fields}

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    edad=forms.IntegerField()
    foto=forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'nombres', 'apellidos','edad','foto')

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')