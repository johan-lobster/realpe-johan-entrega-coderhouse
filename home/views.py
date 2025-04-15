from django.shortcuts import render, redirect
from home.forms import CreacionEstudiante
from home.models import Estudiante

def inicio(request):
    return render(request, 'home/inicio.html')

def crear_estudiante(request):

    if request.method == 'POST':
        formulario = CreacionEstudiante(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            estudiante = Estudiante(nombre = info.get('nombre'), curso = info.get('curso'), nota_final = info.get('nota_final'))
            estudiante.save()
            return redirect('inicio')
    else:
        formulario = CreacionEstudiante()
    return render(request, 'home/crear_estudiante.html', {'formulario':formulario})