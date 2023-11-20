from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.listado_productos, name="productos"),
    path('productos/crear', views.crear_producto, name="crear_producto"),
    path('productos/editar/<int:id>', views.editar_producto, name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name="eliminar_producto"),
    path('AcercaDe', views.Acerca, name="AcercaDe" ),
    path('Contacto',views.crear_contacto, name="Contacto"),
    path('Contacto/ver', views.listado_contacto, name="vercontacto"),
    path('login', views.login, name="login"),
    path('login/crear', views.crear_cuenta, name="crear_cuenta"),
    path('productos/usuario', views.listado_productosu, name="productosu"),
    path('usuario/inicio', views.iniciou, name="iniciou"),
    path('Contacto/usuario', views.crear_contactou, name="Contactou"),
    path('AcercaDe/usuario', views.Acercau, name="AcercaDeu" ),
    path('AcercaDe/inicio', views.Acercai, name="AcercaDei" ),
    path('productos/inicio', views.listado_productosi, name="productosi"),
    path('Contacto/inicio', views.crear_contactoi, name="Contactoi"),
    path('Loginadmin', views.loginadmin, name="loginadmin"),
    path("inicio/admin", views.inicioadmin , name="inicioadmin"),
    path('Contacto/eliminar/<int:id>', views.eliminar_contacto, name="eliminar_contacto"),
    path('Ajustes', views.ajustes, name="ajustes"),
    path('Admin/crear', views.agregar_admin, name='agregaradmin'),
    path('Agregar/Admin', views.crear_usuario_admin, name="AdminCreado"),
    path('Usuarios/ver', views.listado_usuarios, name='usuarios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)