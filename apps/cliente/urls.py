from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-cliente/", views.crear_cliente, name="crear-cliente"),
    path("crear-post/", views.crear_post, name="crear-post"),
]
