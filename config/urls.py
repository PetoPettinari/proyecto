from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include(("home.urls", "home"))),
    path("producto/", include(("apps.producto.producto.urls", "producto"))),
    path("venta/", include(("apps.venta.venta.urls", "venta"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
