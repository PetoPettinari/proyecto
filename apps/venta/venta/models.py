from django.contrib.auth.models import User
from django.db import models


class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nacimiento = models.DateField(null=True)
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    class Meta:
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"

    def __str__(self):
        return f"{self.usuario.username}"

    def get_absolute_url(self):
        return self.avatar.url
