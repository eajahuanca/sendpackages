from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

from correos.utils.db import UpperCharField
from modulos.parametros.models import LogModel

Usuario = get_user_model()

class Pais (LogModel):
    nombre=models.CharField(_('Nombre de Pais'), max_length=50, blank=False, null=False)
    sigla=models.CharField(_('Sigla de Pais'), max_length=10, blank=False, null=False)
    codigo_postal=models.CharField(_('Còdigo Postal'), max_length=50, blank=True, null=True)
    codigo_pais=models.CharField(_('Còdigo de Pais'), max_length=50, blank=False, null=False)
    icono=models.CharField(_('Icono'), max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    

class Departamento (LogModel):
    nombre=models.CharField(_('Nombre del departamento'), max_length=15, blank=False, null=False)
    detalle=models.CharField(_('Detalle del departamento'), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Cargo (LogModel):
    nombre=models.CharField(_('Nombre del cargo'), max_length=50, blank=False, null=False)
    detalle=models.CharField(_('Detalle del cargo'), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Oficina (LogModel):
    nombre=models.CharField(_('Nombre de la oficina'), max_length=50, blank=False, null=False)
    detalle=models.CharField(_('Detalle de la oficina'), max_length=100, blank=True, null=True)
    departamento_id=models.ForeignKey(
        'Departamento', 
        verbose_name=_('Departamento ID'),
        related_name='+',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nombre


class Envio (LogModel):
    pass