from rest_framework import serializers

from .models import (
    Pais,
    Departamento,
    Cargo,
    Oficina,
    Envio
)


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = (
            'id',
            'nombre',
            'sigla',
            'codigo_postal',
            'codigo_pais',
            'icono',
        )


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = (
            #completar campos
        )


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = (
            """completar campos"""
        )


class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = (
            """Completar campos"""
        )

class EnvioSerializer(serializers.ModelSerializer):
    pais = PaisSerializer
    departamento = DepartamentoSerializer
    class Meta:
        model = Envio
        fields = (
            """Completar campos"""
        )