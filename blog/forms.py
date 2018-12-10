from django import forms


class RegistrarProductoForm(forms.Form):
    image=forms.ImageField(label="Foto del producto")
    nombreProducto=forms.CharField(widget=forms.TextInput(),label="Nombre")
    descripcionProducto=forms.CharField(widget=forms.TextInput(),label="Descripción")
    precioProducto=forms.CharField(widget=forms.TextInput(),label="Precio")
    tipoProducto=forms.IntegerField(widget=forms.TextInput(),label="Categoria")


class RegistrarEmpleadoForm(forms.Form):
    rutEmpleado=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordEmpleado=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombreEmpleado=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoEmpleado=forms.CharField(widget=forms.TextInput(),label="Apellido")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")