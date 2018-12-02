from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Empleado(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nombreEmpleado=models.CharField(max_length=30)
    apellidoEmpleado=models.CharField(max_length=30)


class Tienda(models.Model):
    nombreTienda=models.CharField(max_length=30)
    direccionTienda=models.CharField(max_length=30)
    ciudadTienda=models.CharField(max_length=30)
    comunaTienda=models.CharField(max_length=30)
    correoTienda=models.EmailField(max_length=254)