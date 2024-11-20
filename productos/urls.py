from django.urls import path
from productos import views

app_name= 'productos'

urlpatterns = [
    path('cargar/', views.CargarProducto.as_view(), name='CargarProducto'),
    path('ver/', views.VerProducto.as_view(), name='VerProducto'),
    path('ver-extendido/<int:pk>/', views.VerProductoExtendido.as_view(), name='VerProductoExtendido'),
    path('editar/<int:pk>/', views.EditarProducto.as_view(), name='EditarProducto'),
    path('eliminar/<int:pk>/', views.EliminarProducto.as_view(), name='EliminarProducto'),
    path('buscar/', views.buscar, name='buscar'),

]