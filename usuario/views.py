from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.urls import reverse_lazy
from usuario.form import CrearUsuario


def login(request):

    formulario = AuthenticationForm()

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_de_usuario=formulario.cleaned_data.get('username')
            contrasenia=formulario.cleaned_data.get('password')

            usuario=authenticate(username=nombre_de_usuario, password=contrasenia)

            django_login(request, usuario)

            return redirect('inicio:inicio')

    return render(request, 'login.html', {'form': formulario})

def register(request):
    formulario = CrearUsuario()
    if request.method == 'POST':
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('usuarios:login')

    return render(request, 'register.html', {'form': formulario})

def loginn(request):

    formulario = AuthenticationForm()

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_de_usuario=formulario.cleaned_data.get('username')
            contrasenia=formulario.cleaned_data.get('password')

            usuario=authenticate(username=nombre_de_usuario, password=contrasenia)

            django_login(request, usuario)

            return redirect('productos:ver')

    return render(request, 'registrarse.html', {'form': formulario})