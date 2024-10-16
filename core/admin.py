from django.contrib import admin # type: ignore
from .models import Persona, Auto

# Register your models here.

admin.site.register(Persona)
admin.site.register(Auto)