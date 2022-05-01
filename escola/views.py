from rest_framework import viewsets, generics
from escola.models import Alune, Curso, Matricula
from escola.serializer import AluneSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAluneSerializer


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


class ListaMatriculasAlune(generics.ListAPIView):
    """Listando todas as matriculas"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(alune_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAluneSerializer
