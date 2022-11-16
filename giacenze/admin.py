from django.contrib import admin

# Register your models here.
from .models import Pc, Telefono

admin.site.register(Pc)
admin.site.register(Telefono)