from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=25)
    curso = models.CharField(max_length=25)
    nota_final = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre},{self.curso},{self.nota_final}'