from tabnanny import verbose
from django.db import models

# Create your models here.

class Empresa(models.Model):
    empresa = models.CharField('Nombre Empresa', max_length=50)
    cuit = models.DecimalField('Cuit', max_digits=11, decimal_places=0)
    direccion = models.CharField('Dirección', max_length=50)
    telefono = models.DecimalField('Contacto', max_digits=13,decimal_places=0)
    email = models.EmailField('Email', blank=True)
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add= True)
    

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    
    def __str__(self):
        return self.empresa


class Maquina(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, blank=False)
    tipo = models.CharField('Tipo Maquinaria', max_length=50)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    serie = models.CharField('N° Serie', max_length=50, blank=True)
    iden_empres = models.CharField('Iden interno de Empresa', max_length=50, blank=True)


    class Meta:
        verbose_name = 'Maquina'
        verbose_name_plural = 'Maquinas'

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.empresa, self.tipo, self.marca, self.modelo)    

class Presupuesto(models.Model):
    cantidad = models.DecimalField('Cantidad', max_digits=3, decimal_places=2)
    iten = models.CharField('Descripción Iten', max_length=100)
    p_unitad = models.DecimalField('Precio Unitario', max_digits=6, decimal_places=2)
   

    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'

    def __str__(self):
        return "{0},{1},{2}".format(self.cantidad, self.iten, self.p_unitad)