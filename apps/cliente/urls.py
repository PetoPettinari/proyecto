from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-cliente/", views.crear_cliente, name="crear-cliente"),
    path("crear-post/", views.crear_post, name="crear-post"),
    path("crear-autor/", views.crear_autor, name="crear-autor"),
]
