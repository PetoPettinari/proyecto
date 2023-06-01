from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.CharField(max_length=50, null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Post(models.Model):
    modelo = models.TextField(max_length=100)
    instrumento = models.TextField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.modelo} {self.instrumento}"


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.CharField(max_length=50, null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
