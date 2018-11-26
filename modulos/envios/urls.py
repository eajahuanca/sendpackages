from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PaisView,
    DepartamentoView,
    #CargoView,
    #OficinaView,
    EnvioView,
    EnvioViewDetail
)

router = DefaultRouter()
#router.register('nombre_ruta', OBJETOViewSet , base_name='nombre_ruta')

urlpatterns = [
    #path('api/', include(router.urls)),
    path('api/pais', PaisView.as_view(), name='pais'),
    path('api/departamento', DepartamentoView.as_view(), name='departamento'),
    #path('api/cargo', DepartamentoView.as_view(), name='cargo'),
    #path('api/oficina', DepartamentoView.as_view(), name='oficina'),
    path('api/envio', EnvioView.as_view(), name='envio'),
    path('api/envioDetalle/<int:pk>', EnvioViewDetail.as_view(), name='envio_detalle'),
]