from django import forms # type: ignore
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'edad', 'telefono', 'correo', 'direccion', 'tipo', 'activo']
