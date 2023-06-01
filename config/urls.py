from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include(("home.urls", "home"))),
    path("producto/", include(("apps.producto.producto.urls", "producto"))),
    path("venta/", include(("apps.venta.venta.urls", "venta"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
]
