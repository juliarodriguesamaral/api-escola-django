from rest_framework import viewsets
from escola.models import Alune, Curso, Matricula
from escola.serializer import AluneSerializer, CursoSerializer, MatriculaSerializer


class AlunesViewSet(viewsets.ModelViewSet):
    """Exibindo todes alunes"""
    queryset = Alune.objects.all()
    serializer_class = AluneSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
