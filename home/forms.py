from django import forms

class CreacionEstudiante(forms.Form):
    nombre = forms.CharField(max_length=25)
    curso = forms.CharField(max_length=25)
    nota_final = forms.CharField(max_length=10)