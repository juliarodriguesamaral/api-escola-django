from django.contrib import admin
from django.urls import path, include
from escola.views import AlunesViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAlune, \
    ListaAlunesComMatriculaEmUmCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunes', AlunesViewSet, basename='Alunes')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunes/<int:pk>/matriculas/', ListaMatriculasAlune.as_view()),
    path('cursos/<int:pk>/alunes/', ListaAlunesComMatriculaEmUmCurso.as_view())
]
