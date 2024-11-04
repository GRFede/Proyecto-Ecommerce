from django.shortcuts import render,redirect
from inicio.models import Personas, Productos
from inicio.form import CrearUsuario, CrearProducto, BuscarProducto



def inicio(request):
    return render(request, 'inicio.html')

def crear_usuario(request):
    formulario = CrearUsuario()

    if request.method == 'POST':
        formulario = CrearUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data
            persona=Personas(nombres=data.get('nombres'),apellidos=data.get('apellidos'),nacimiento=data.get('fecha nachimiento'),foto=data.get('imagen'))
            persona.save()
            return redirect('crear_usuario.html')

    return render(request, 'crear_usuario.html', {'form':formulario})

def cargar_producto(request):
            formulario = CrearProducto()
            if request.method == 'POST':
                formulario = CrearProducto(request.POST, request.FILES)
                if formulario.is_valid():
                    data=formulario.cleaned_data
                    producto=Productos(nombres_producto=data.get('nombres producto'),descripcion_breve_producto=data.get('descripcion breve producto'),descripcion_extendida_producto=data.get(' descripcion extendida producto'),precio=data.get('precio'),imagen_producto=data.get('imagen producto'),categoria_producto=data.get('categoria producto(hogar/construccion)'))
                    producto.save()
                    return redirect('crear_usuario.html')

            return render(request, 'cargar_producto.html', {'form':formulario})

def buscar_producto(request):

    formulario = BuscarProducto(request.GET)
    if formulario.is_valid():
        nombres_producto=formulario.cleaned_data.get('nombre_producto')

        producto=Productos.objects.filter()
    else:
        producto=Productos.objects.all()  

    return render(request, 'buscar_producto.html', {'producto' : producto, 'form': formulario})

def ver_producto(request,id):
    producto=Productos.objects.get(id=id)
    return(request, 'ver_producto.html', {'producto':producto})

def eliminar_producto(request):
    return 




def hogar(request):
    return 
def construccion(request):
    return 
