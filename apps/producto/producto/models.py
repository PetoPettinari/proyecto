from django.db import models


class ProductoCategoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):

    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoría")    
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        
    def __str__(self) -> str:
        return f"{self.nombre} - {self.categoria} - ${self.precio:.2f}"
    