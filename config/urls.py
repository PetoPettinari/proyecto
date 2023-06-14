from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
    path("producto.producto/", include(("producto.producto.urls", "producto"))),
    path("venta.venta/", include(("venta.venta.urls", "venta"))),
]

#! Este código es válido en un entorno de desarrollo (DEBUG=True). Noo utilizarlo en un entorno de producción.
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
