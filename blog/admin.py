from django.contrib import admin
from .models import Empleado
# Register your models here.
class AdminEmpleado(admin.ModelAdmin):
    list_display = ["nombreEmpleado", "apellidoEmpleado"]
    class Meta:
        model = Empleado


admin.site.register(Empleado, AdminEmpleado)