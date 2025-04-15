from django.urls import path
from home.views import inicio
from home.views import crear_estudiante

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('estudiante/crear', crear_estudiante, name = 'crear_estudiante')
]