from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name= 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]