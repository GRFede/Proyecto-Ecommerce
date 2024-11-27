from django.shortcuts import render,redirect
from inicio.models import Personas


def inicio(request):
    return render(request, 'inicio.html')

def about(request):

    return render(request, 'about.html', {})
