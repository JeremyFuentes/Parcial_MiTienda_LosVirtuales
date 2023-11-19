from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50, verbose_name="Producto")
    categoria = models.TextField(null=False, max_length=50, verbose_name="Categoria")
    descripcion = models.TextField(null=False, max_length=200, verbose_name="Descripcion")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    existencias = models.IntegerField(null=False, verbose_name="Existencia")
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=9, verbose_name="Precio")
    
    def __str__(self) -> str:
        fila = "Nombre: " + self.nombre + " - " + "Descipcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=100, verbose_name="Nombre")
    correo = models.EmailField(null=False, max_length=50, verbose_name="Correo")
    celular = models.IntegerField(null=False, verbose_name="Celular")
    Descripcion = models.TextField(null=False, verbose_name="Descripcion")
    
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50, verbose_name="Nombre")
    Apellido = models.TextField(null=False, max_length=500, verbose_name="Apellido")
    correo = models.EmailField(unique=True, null=False, max_length=50, verbose_name="Correo")
    Contraseña = models.CharField(null=False, max_length=50, verbose_name="Contraseña")
    
class Admin(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50, verbose_name="Nombre Admin")
    Apellido = models.TextField(null=False, max_length=500, verbose_name="Apellido Admin")
    correo = models.EmailField(unique=True, null=False, max_length=50, verbose_name="Correo Admin")
    Contraseña = models.CharField(null=False, max_length=50, verbose_name="Contra Admin")
    celular = models.IntegerField(null=False, verbose_name="Celular Admin")
    Direccion = models.TextField(null=False, verbose_name="Direc Admin")