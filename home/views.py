from django.shortcuts import render

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_estudiante(request):
    return render(request, 'home/crear_estudiante.html')