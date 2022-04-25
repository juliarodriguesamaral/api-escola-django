from rest_framework import viewsets
from escola.models import Alune, Curso
from escola.serializer import AluneSerializer, CursoSerializer


class AlunesViewSet(viewsets.ModelViewSet):
    """Exibindo todes alunes"""
    queryset = Alune.objects.all()
    serializer_class = AluneSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
