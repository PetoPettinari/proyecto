from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


# * Login basado en funciones
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(
                    request,
                    "home/index.html",
                    {"mensaje": f"Se ha logueado correctamente."},
                )
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})


# * Registro basado en funciones
from django.contrib.admin.views.decorators import staff_member_required

from . import forms


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Vendedor creado 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")
