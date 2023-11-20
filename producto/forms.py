from django import forms
from .models import Productos, Contacto, Usuarios, Admin

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
        
class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"
        
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"