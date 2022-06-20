from django.contrib import admin

from empresa.models import *
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Maquina)
admin.site.register(Presupuesto)