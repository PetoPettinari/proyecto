from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
    path(
        "productocategoria/detail/<int:pk>",
        views.ProductoCategoriaDetail.as_view(),
        name="productocategoria_detail",
    ),
    path(
        "productocategoria/list/",
        views.productoCategoriaList.as_view(),
        name="productocategoria_list",
    ),
    path(
        "productocategoria/create/",
        staff_member_required(views.producto_categoria_create.as_view()),
        name="productocategoria_create",
    ),
    path(
        "productocategoria/delete/<int:pk>",
        staff_member_required(views.producto_categoria_delete.as_view()),
        name="productocategoria_delete",
    ),
    path(
        "productocategoria/update/<int:pk>",
        staff_member_required(views.ProductoCategoriaUpdate.as_view()),
        name="productocategoria_update",
    ),
]
