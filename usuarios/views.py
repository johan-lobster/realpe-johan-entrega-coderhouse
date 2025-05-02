from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FromularioEdicionPerfil
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)

            return redirect("inicio")
    else:
        formulario = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect("login")
    else:
        formulario = FormularioRegistro()

    return render(request, 'usuarios/registro.html', {'formulario': formulario})


@login_required
def editar_perfil(request):
    if request.method == "POST":
        formulario = FromularioEdicionPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()

            return redirect("inicio")
    else:
        formulario = FromularioEdicionPerfil(instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})