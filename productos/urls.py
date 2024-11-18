from django.urls import path
from productos import views

app_name= 'productos'

urlpatterns = [
    path('cargar/', views.CargarProducto.as_view(), name='CargarProducto'),
    path('ver/', views.VerProducto.as_view(), name='VerProducto'),
    path('buscar/', views.buscar, name='buscar'),
    path('borrar/', views.borrar, name='borrar'),
    path('editar/', views.editar, name='editar'),

]