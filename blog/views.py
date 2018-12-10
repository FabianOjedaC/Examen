from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests 
from .models import Producto, Tienda
from .forms import RegistrarProductoForm, RegistrarEmpleadoForm, LoginForm
from django.contrib.auth.models import User
from .serializers import ProductoSerializer, UserSerializer, TiendaSerializer
from rest_framework import viewsets
# Create your views here.

def index(request):
    response = requests.get('https://mindicador.cl/api')
    geodata = response.json()
    return render(request, 'index.html', {
        'dolar': geodata['dolar'],
    })

def salir(request):
    logout(request)
    return redirect('index/')

def registroProducto(request):
    actual=request.user
    producto=Producto.objects.all()
    form=RegistrarProductoForm(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Producto(image=data.get("image"),nombreProducto=data.get("nombreProducto"),descripcionProducto=data.get("descripcionProducto"),
        precioProducto=data.get("precioProducto"),tipoProducto=data.get("tipoProducto"))
        regDB.save()
    form = RegistrarProductoForm()
    return render(request, "registroProducto.html", {'form': form, 'actual':actual,'titulo':"Registro Producto",})

def ingreso(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'login.html',{'form':form,'titulo':'Ingreso Usuario',})

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer