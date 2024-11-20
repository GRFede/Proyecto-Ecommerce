from django.shortcuts import render,redirect
from productos.models import Productos
from productos.form import CrearProducto, BuscarProducto
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CargarProducto(LoginRequiredMixin, CreateView):
    model=Productos
    template_name = "cargar.html"
    success_url = reverse_lazy('productos:VerProducto')
    fields = ['nombres_producto',
            'descripcion_breve_producto',
            'descripcion_extendida_producto',
            'precio',
            'imagen_producto',
            'categoria_producto',
            ]

class VerProducto(ListView):
    model=Productos
    template_name = "ver.html"
    context_object_name = 'productos'

class VerProductoExtendido(DetailView):
    model=Productos
    template_name = "ver_extendido.html"

class EliminarProducto(LoginRequiredMixin, DeleteView):
    model=Productos
    template_name = "eliminar.html"
    success_url=reverse_lazy('productos:VerProducto')



class EditarProducto(LoginRequiredMixin, UpdateView):
    model=Productos
    template_name = "editar.html"
    success_url = reverse_lazy('productos:VerProducto')
    fields = ['nombres_producto',
            'descripcion_breve_producto',
            'descripcion_extendida_producto',
            'precio',
            'imagen_producto',
            'categoria_producto',
            ]
    

def buscar(request):

    formulario = BuscarProducto(request.GET)
    if formulario.is_valid():
        nombres_producto=formulario.cleaned_data.get('nombre_producto')

        producto=Productos.objects.filter()
    else:
        producto=Productos.objects.all()  

    return render(request, 'buscar.html', {'producto' : producto, 'form': formulario})