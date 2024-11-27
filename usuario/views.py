from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from usuario.form import Usuario, FormularioEdicion, FormularioCambioPassword
from django.contrib.auth.views import PasswordChangeView
from usuario.models import Info



def register(request):
    formulario = Usuario()
    if request.method == 'POST':
        formulario = Usuario(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('usuarios:registrarse')

    return render(request, 'register.html', {'form': formulario})

def loginn(request):

    formulario = AuthenticationForm()

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():

            usuario=formulario.get_user()

            login(request, usuario)

            Info.objects.get_or_create(user=usuario)

            return redirect('inicio:inicio')

    return render(request, 'registrarse.html', {'form': formulario})

def editar_perfil(request):
    
    info = request.user.info

    formulario = FormularioEdicion(instance=request.user, initial = {'avatar': info.avatar})

    if request.method == 'POST':

        formulario = FormularioEdicion(request.POST,request.FILES, instance=request.user)

        if formulario.is_valid():

            info.avatar = formulario.cleaned_data.get('avatar') if formulario.cleaned_data.get('avatar') else info.avatar
            info.save()

            formulario.save()

            return redirect('inicio:inicio')

    return render(request, 'perfil.html', {'form': formulario})


    
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'cambiar_contraseña.html'
    success_url = reverse_lazy('usuarios:contraseña_exitoso')

def contraseña_exitoso(request):
    return render(request, 'contraseña_exitoso.html', {})