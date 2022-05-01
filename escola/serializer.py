from rest_framework import serializers
from escola.models import Alune, Curso, Matricula


class AluneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alune
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
