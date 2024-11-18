from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
]