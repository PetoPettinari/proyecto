from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# *
# * Inicio
# *


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "producto/index.html")

    # class IndexView(TemplateView):
    template_name = productoCategoriaList


# *
# * List
# *


# def producto_categoria_list(request):
#     """Falta la consulta"""
#     categorias = models.ProductoCategoria.objects.all()
#     context = {"categorias": categorias}
#     return render(request, "producto/productocategoria_list.html", context)


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(
                nombre__icontains=query
            )
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list


# *
# * Create
# *


# def producto_categoria_create(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:index")
#     else:
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto.producto:index")


# *
# * Delete
# *

# def producto_categoria_delete(request: HttpRequest, pk) -> HttpResponse:
#     categoria = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_confirmdelete.html", {"categoria": categoria})


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")


# *
# * Update
# *


# def producto_categoria_update(request: HttpRequest, pk) -> HttpResponse:
#     categoria = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:
#         form = forms.ProductoCategoriaForm(instance=categoria)
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    form_class = forms.ProductoForm


# *
# * Detail
# *


def ProductoCategoriaDetail(request: HttpRequest, pk) -> HttpResponse:
    categoria = models.ProductoCategoria.objects.get(id=pk)
    return render(
        request, "producto/productocategoria_detail.html", {"object": categoria}
    )


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria

class productolist(ListView):
    model = models.Producto
   
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:index") 
    
    