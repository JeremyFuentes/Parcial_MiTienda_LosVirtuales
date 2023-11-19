from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Productos, Contacto
from .forms import ProductosForm, ContactoForm, UsuariosForm

# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')

def Acerca(request):
    return render(request, 'AcercaDe/AcercaDe.html')

def contacto(request):
    return render(request, 'Contacto/Contacto.html')

def login(request):
    return render(request, 'login/login.html')

def crear_cuenta(request):
    return render(request, 'login/Crearcuenta.html')

def listado_productos(request):
    #Crear variable para almacenar los prodcutos
    productos = Productos.objects.all()
    return render(request, 'producto/productos.html', {'productos': productos})

def crear_producto(request):
    formulario = ProductosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'producto/crear.html', {'formulario': formulario})

def editar_producto(request, id):
    producto = Productos.objects.get(id = id)
    formulario = ProductosForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'producto/editar.html', {'formulario': formulario})

def eliminar_producto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('productos')

def listado_contacto(request):
    #Crear variable para almacenar los prodcutos
    contactos = Contacto.objects.all()
    return render(request, 'Contacto/vercontacto.html', {'contactos': contactos})

def crear_contacto(request):
    formcont = ContactoForm(request.POST or None)
    if formcont.is_valid():
       formcont.save()
       return redirect('Contacto')
    return render(request, 'Contacto/Contacto.html', {'formcont':formcont})

def crear_cuenta(request):
    formusu = UsuariosForm(request.POST or None)
    if formusu.is_valid():
       formusu.save()
       return redirect('login')
    return render(request, 'login/Crearcuenta.html', {'formusu':formusu})

