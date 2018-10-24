from datetime import datetime as dt
from django.utils.translation import ugettext as _
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from correos.response import ErrorRestResponse, SuccessRestResponse
from correos.viewsets import ViewSet
from correos.views import APIView
from .serializer import (
    PaisSerializer,
    DepartamentoSerializer,
    CargoSerializer,
    OficinaSerializer,
    EnvioSerializer
)
from .models import (
    Pais,
    Departamento,
    Cargo,
    Oficina,
    Envio
)

class PaisView(APIView):
    """Listar todos los paises"""
    def get(self, request, *args, **kargs):
        paises = Pais.objects.filter(fecha_eliminacion___isnull=True)
        serializer = PaisSerializer(paises, many=True)
        return Response(serializer.data)
    
    """Registra un nuevo pais"""
    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario_creacion=request.user.id, fecha_eliminacion=dt.now())
            return SuccessRestResponse(_('Registro agregado de manera correcta'), status=status.HTTP_201_CREATED, data=serializer.data)
        return ErrorRestResponse(_('Tiene los siguientes errores'),status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DepartamentoView(APIView):
    pass


class CargoView(APIView):
    pass


class OficinaView(APIView):
    pass