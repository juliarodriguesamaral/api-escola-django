from rest_framework import viewsets, generics
from escola.models import Alune, Curso, Matricula
from escola.serializer import AluneSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAluneSerializer,\
    ListaAlunesComMatriculaEmUmCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunesViewSet(viewsets.ModelViewSet):
    """Exibindo todes alunes"""
    queryset = Alune.objects.all()
    serializer_class = AluneSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAlune(generics.ListAPIView):
    """Listando todas as matriculas"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(alune_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAluneSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunesComMatriculaEmUmCurso(generics.ListAPIView):
    """Listando alunes que possuem matricula em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunesComMatriculaEmUmCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
