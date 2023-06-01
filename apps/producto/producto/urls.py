from django.urls import path

from . import views

# *********** URLS basadas en funciones
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "producto_categoria_listado/",
        views.productoCategoriaList,
        name="productoCategoriaList",
    ),
    path(
        "producto_categoria_create/",
        views.producto_categoria_create,
        name="producto_categoria_create",
    ),
    path(
        "producto_categoria_delete/<int:id>",
        views.producto_categoria_delete,
        name="producto_categoria_delete",
    ),
    path(
        "producto_categoria_update/<int:id>",
        views.producto_categoria_delete,
        name="producto_categoria_delete",
    ),
    path(
        "productocategoria/detail/<int:pk>",
        views.producto_categoria_detail,
        name="productocategoria_detail",
    ),
]

# *********** URLS basadas en clases
"""urlpatterns += [
    # path("", views.IndexView.as_view(), name="index"),
    path(
        "productocategoria/list/",
        views.ProductoCategoriaList.as_view(),
        name="productocategoria_list",
    ),
    path(
        "productocategoria/create/",
        views.ProductoCategoriaCreate.as_view(),
        name="productocategoria_create",
    ),
    path(
        "productocategoria/delete/<int:pk>",
        views.ProductoCategoriaDelete.as_view(),
        name="productocategoria_delete",
    ),
    path(
        "productocategoria/update/<int:pk>",
        views.ProductoCategoriaUpdate.as_view(),
        name="productocategoria_update",
    ),
    path(
        "productocategoria/detail/<int:pk>",
        views.ProductoCategoriaDetail.as_view(),
        name="productocategoria_detail",
    ),
]"""
