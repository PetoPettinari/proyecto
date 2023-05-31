from django.shortcuts import render

from . import forms


def index(request):
    return render(request, "cliente/index.html")


def crear_autor(request):
    form = forms.Autorform()
    context = {"form": form}
    return render(request, "cliente/crear_cliente.html")
