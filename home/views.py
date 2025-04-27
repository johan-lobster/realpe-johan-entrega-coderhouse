from django.shortcuts import render, redirect
from home.forms import CreacionEstudiante
from home.models import Estudiante
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'home/lista_estudiantes.html', {'estudiantes':estudiantes})

#def detalle_estudiante(request, estudiante_especifico):
#    estudiante = Estudiante.objects.get(id = estudiante_especifico)
#    return render(request, 'home/detalle_estudiante.html', {'estudiante':estudiante})

class VistaDetalleEstudiante(DetailView):
    model = Estudiante
    template_name = "home/detalle_estudiante.html"

class VistaModificarEstudiante(UpdateView):
    model = Estudiante
    template_name = "home/modificar_estudiante.html"
    fields = ["nombre", "curso", "nota_final"]
    success_url = reverse_lazy('lista_estudiantes')
