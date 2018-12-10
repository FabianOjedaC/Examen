from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Empleado(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, db_index=True)
    nombreEmpleado=models.CharField(max_length=30)
    apellidoEmpleado=models.CharField(max_length=30)


class Tienda(models.Model):
    nombreTienda=models.CharField(max_length=30)
    direccionTienda=models.CharField(max_length=30)
    ciudadTienda=models.CharField(max_length=30)
    comunaTienda=models.CharField(max_length=30)
    correoTienda=models.EmailField(max_length=254)
    empleado=models.CharField(max_length=30)

class Producto(models.Model):
    image=models.ImageField(upload_to = 'static/media/')
    nombreProducto=models.CharField(max_length=30)
    descripcionProducto=models.CharField(max_length=30)
    precioProducto=models.CharField(max_length=30)
    tipoProducto=models.CharField(max_length=30)

def __str__(self):
 return self.nombreProducto