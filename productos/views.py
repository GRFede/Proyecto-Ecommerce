from django.shortcuts import render,redirect
from productos.models import Productos
from productos.form import CrearProducto, BuscarProducto
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.

class CargarProducto(CreateView):
    model=Productos
    template_name = "cargar.html"
    success_url = reverse_lazy('productos:VerProducto')
    fields = ['nombres_producto','descripcion_breve_producto','descripcion_extendida_producto','precio','imagen_producto','categoria_producto']

class VerProducto(ListView):
    model=Productos
    template_name = "ver.html"
    context_object_name = 'productos'

def cargar(request):
            formulario = CrearProducto()

            if request.method == 'POST':
                
                formulario = CrearProducto(request.POST, request.FILES)
                if formulario.is_valid():
                    data=formulario.cleaned_data
                    producto=Productos(nombres_producto=data.get('nombres producto'),descripcion_breve_producto=data.get('descripcion breve producto'),descripcion_extendida_producto=data.get(' descripcion extendida producto'),precio=data.get('precio'),imagen_producto=data.get('imagen producto'),categoria_producto=data.get('categoria producto'))
                    producto.save()
                    return redirect('productos:buscar')

            return render(request, 'cargar.html', {'form':formulario})

def buscar(request):

    formulario = BuscarProducto(request.GET)
    if formulario.is_valid():
        nombres_producto=formulario.cleaned_data.get('nombre_producto')

        producto=Productos.objects.filter()
    else:
        producto=Productos.objects.all()  

    return render(request, 'buscar.html', {'producto' : producto, 'form': formulario})

def ver(request,id):
    producto=Productos.objects.get(id=id)
    return(request, 'ver.html', {'producto':producto})

def borrar(request):
    return 
def editar(request):
    return