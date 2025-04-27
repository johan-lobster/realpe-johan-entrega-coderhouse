from django.urls import path
from home.views import inicio, crear_estudiante, lista_estudiantes, VistaDetalleEstudiante, VistaModificarEstudiante


urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('estudiantes/' , lista_estudiantes, name = 'lista_estudiantes'),
    path('estudiante/crear/', crear_estudiante, name = 'crear_estudiante'),
    path('estudiantes/<int:pk>/', VistaDetalleEstudiante.as_view(),name= 'detalle_estudiante'),
    path('estudiantes/<int:pk>/modificar-estudiante/', VistaModificarEstudiante.as_view(), name='modificar_estudiante')
]