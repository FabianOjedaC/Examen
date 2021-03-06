from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Producto, Tienda



class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('image', 'nombreProducto', 'descripcionProducto', 'tipoProducto', 'precioProducto')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('correoTienda', 'nombreTienda', 'direccionTienda', 'ciudadTienda', 'comunaTienda','empleado')