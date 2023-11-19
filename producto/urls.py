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
    path('login/crear', views.crear_cuenta, name="crear_cuenta")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)