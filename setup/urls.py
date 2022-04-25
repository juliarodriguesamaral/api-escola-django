from django.contrib import admin
from django.urls import path, include
from escola.views import AlunesViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunes', AlunesViewSet, basename='Alunes')
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
