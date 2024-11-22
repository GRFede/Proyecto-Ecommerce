from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name= 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register , name='register'),
    path('registrarse/', views.loginn, name='registrarse'),
    path('perfil/', views.UsuarioEdicion.as_view(), name='perfil'),
    path('cambiar-contraseña/', views.CambioPassword.as_view(), name='cambiar_contraseña'),
    path('cambio-contraseña-exitoso/', views.contraseña_exitoso, name='contraseña_exitoso'),



]