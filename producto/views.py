from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Productos, Contacto, Admin, Usuarios
from .forms import ProductosForm, ContactoForm, UsuariosForm, AdminForm


# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')

def iniciou(request):
    return render(request, 'usuario/inicio.html')

def inicioadmin(request):
    return render(request, 'producto/inicio.html')

def Acerca(request):
    return render(request, 'AcercaDe/AcercaDe.html')

def Acercau(request):
    return render(request, 'usuario/acercadeu.html')

def Acercai(request):
    return render(request, 'pages/acercade.html')

def ProductosU(request):
    return render(request, 'usuario/productos.html')

def Productosi(request):
    return render(request, 'pages/productos.html')

def contactou(request):
    return render(request, 'usuario/contacto.html')

def contactoi(request):
    return render(request, 'pages/contacto.html')

def contacto(request):
    return render(request, 'Contacto/Contacto.html')

def login(request):
    return render(request, 'login/login.html')

def loginadmin(request):
    return render(request, 'loginadmin/login.html')

def ajustes(request):
    return render(request, 'loginadmin/ajustes.html')


def crear_cuenta(request):
    return render(request, 'login/Crearcuenta.html')

def agregar_admin(request):
    return render(request, 'loginadmin/Crearcuenta.html')

def listado_productos(request):
    #Crear variable para almacenar los productos
    productos = Productos.objects.all()
    return render(request, 'producto/productos.html', {'productos': productos})

def listado_productosu(request):
    #Crear variable para almacenar los prodcutos
    productosu = Productos.objects.all()
    return render(request, 'usuario/productos.html', {'productosu': productosu})

def listado_productosi(request):
    #Crear variable para almacenar los productos
    productosi = Productos.objects.all()
    return render(request, 'pages/productos.html', {'productosi': productosi})

def listado_usuarios(request):
    #Crear variable para almacenar los prodcutos
    usuarios = Usuarios.objects.all()
    return render(request, 'loginadmin/verusuario.html', {'usuario': usuarios})

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

def eliminar_contacto(request, id):
    producto = Contacto.objects.get(id=id)
    producto.delete()
    return redirect('vercontacto')

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

def crear_contactou(request):
    formcontu = ContactoForm(request.POST or None)
    if formcontu.is_valid():
       formcontu.save()
       return redirect('Contactou')
    return render(request, 'usuario/contacto.html', {'formcontu':formcontu})

def crear_contactoi(request):
    formconti = ContactoForm(request.POST or None)
    if formconti.is_valid():
       formconti.save()
       return redirect('Contactoi')
    return render(request, 'pages/contacto.html', {'formconti':formconti})

def crear_usuario_admin(request):
    formadmin = AdminForm(request.POST or None)
    if formadmin.is_valid():
       formadmin.save()
       return redirect('AdminCreado')
    return render(request, 'loginadmin/Crearcuenta.html', {'formadmin':formadmin})

def crear_cuenta(request):
    formusu = UsuariosForm(request.POST or None)
    if formusu.is_valid():
       formusu.save()
       return redirect('login')
    return render(request, 'login/Crearcuenta.html', {'formusu':formusu})

