from django.contrib import admin
from .models import Empleado, Tienda, Producto
# Register your models here.
class AdminEmpleado(admin.ModelAdmin):
    class Meta:
        model = Empleado


admin.site.register(Empleado, AdminEmpleado)

class AdminTienda(admin.ModelAdmin):
    list_display = ["nombreTienda", "correoTienda"]
    class Meta:
        model = Tienda


admin.site.register(Tienda, AdminTienda)

class AdminProducto(admin.ModelAdmin):
    list_display = ["nombreProducto", "descripcionProducto"]
    class Meta:
        model = Producto


admin.site.register(Producto, AdminProducto)