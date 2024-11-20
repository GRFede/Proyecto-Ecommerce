from django.shortcuts import render,redirect
from inicio.models import Personas
from inicio.form import CrearUsuario



def inicio(request):
    return render(request, 'inicio.html')

def crear_usuario(request):
    formulario = CrearUsuario()

    if request.method == 'POST':
        formulario = CrearUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data
            persona=Personas(nombres=data.get('nombres'),apellidos=data.get('apellidos'),edad=data.get('edad'),foto=data.get('imagen'))
            persona.save()
            return redirect('usuarios:login')

    return render(request, 'crear_usuario.html', {'form':formulario})

def about(request):

    return render(request, 'about.html', {})
