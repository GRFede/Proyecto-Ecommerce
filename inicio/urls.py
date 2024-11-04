from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('cargar-producto/', views.cargar_producto, name='cargar_producto'),
    path('ver-producto/<int:id>', views.ver_producto, name='ver_producto'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('eliminar-producto/', views.eliminar_producto, name='eliminar_producto'),

    path('hogar/', views.hogar, name='hogar'),
    path('construccion/', views.construccion, name='construccion'),
]