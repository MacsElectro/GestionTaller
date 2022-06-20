from tabnanny import verbose
from django.db import models

# Create your models here.

class Empresa(models.Model):
    empresa = models.CharField(max_length=50)
    cuit = models.DecimalField(max_digits=11, decimal_places=0)
    direccion = models.CharField(max_length=50)
    telefono = models.DecimalField(max_digits=13,decimal_places=0)
    email = models.EmailField()
    fecha = models.DateField(auto_now=False, auto_now_add= True)
    
    class Meta:
        verbose_name = 'Empresa'
    
    def __str__(self):
        return self.empresa


class Maquina(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    iden_empres = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Maquina'

class Presupuesto(models.Model):
    cantidad = models.DecimalField(max_digits=3, decimal_places=2)
    iten = models.CharField(max_length=100)
    p_unitad = models.DecimalField(max_digits=6, decimal_places=2)
    p_total = models.DecimalField(max_digits=6, decimal_places=2)

