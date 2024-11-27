from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm


class Usuario(UserCreationForm):
        
    first_name=forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput())
    last_name=forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput())
    avatar=forms.ImageField(label='Foto', required=False)
    email=forms.EmailField(widget=forms.EmailInput())
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'email', 'password1', 'password2']
        help_texts= {key: '' for key in fields}

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput())
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput())
    avatar=forms.ImageField(label='Foto', required=False)

    class Meta: 
        model = User
        fields = ['email', 'username', 'first_name', 'last_name','avatar']
        help_texts= {key: '' for key in fields}

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"), widget=forms.PasswordInput())
    new_password1 = forms.CharField(label=("Nueva Contraseña"), widget=forms.PasswordInput())
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']