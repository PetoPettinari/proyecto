from django.shortcuts import render

from . import forms


def index(request):
    context = {"forms": forms}
    return render(request, "cliente/index.html", context)


def crear_autor(request):
    if request.method == "POST":
        form = form.AutorForm(request.POST)
        if form.is_valid():
            form.save()("cliente:index")
    else:
        form = forms.Autorform()
    return render(request, "cliente/crear_cliente.html", {"form": form})


def crear_post(request):
    if request.method == "POST":
        form = form.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return "cliente:index"
    else:
        form = forms.Postform()
    return render(request, "cliente/crear_cliente.html", {"form": form})


def crear_cliente(request):
    if request.method == "cliente":
        form = form.AutorForm(request.cliente)
        if form.is_valid():
            form.save()("cliente:index")
    else:
        form = forms.Autorform()
    return render(request, "cliente/crear_cliente.html", {"form": form})
