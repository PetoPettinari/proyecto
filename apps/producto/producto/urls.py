from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
    path(
        "productocategoria/detail/<int:pk>",
        views.ProductoCategoriaDetail.as_view(),
        name="ProductoCategoriaDetail",
    ),
    path(
        "productocategoria/list/",
        views.ProductoCategoriaList.as_view(),
        name="ProductoCategorialist",
    ),
    path(
        "productocategoria/create/",
        staff_member_required(views.ProductoCategoriaCreate.as_view()),
        name="ProductoCategoriaCreate",
    ),
    path(
        "productocategoria/delete/<int:pk>",
        staff_member_required(views.ProductoCategoriaDelete.as_view()),
        name="ProductoCategoriaDelete",
    ),
    path(
        "productocategoria/update/<int:pk>",
        staff_member_required(views.ProductoCategoriaUpdate.as_view()),
        name="ProductoCategoriaUpdate",
    ),
    path("Producto/create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("Producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("Producto/detail/<int:pk>", views.Productodetail.as_view(), name="producto_detail"),
    path("Producto/delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
    path("Producto/update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),    
]
