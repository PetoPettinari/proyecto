from django.contrib import admin

from . import models

admin.site.site_title = "producto"
admin.site.site_header = " INSTRUMENTOS MUSICALES "


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    """
    - list_display: tupla que especifica los campos que se mostrarán en la lista de objetos
    - search_fields: tupla que especifica los campos por los que se puede buscar en la lista de objetos
    - list_filter: tupla que especifica los campos por los que se puede filtrar en la lista de objetos
    - ordering: tupla que especifica el orden en que se mostrarán los objetos
    """

    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)

    @admin.register(
        models.ProductoCategoria, product_class=models.ProductoCategoriaAdmin
    )
    class ProductoAdmin(admin.ModelAdmin):
        list_display = (
            "categoria",
            "nombre",
            "modelo",
            "cantidad",
            "precio",
            "descripcion",
            "fecha_actualizacion",
        )

    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre",
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"
