from django.contrib import admin
from django.urls import path, include
from escola.views import (
    EstudanteViewSet,
    CursoViewSet,
    MatriculaViewSet,
    ListaMatriculasEstudanteView,
    ListaMatriculasCursoView,
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("estudantes", EstudanteViewSet, basename="Estudante")
router.register("cursos", CursoViewSet, basename="Curso")
router.register("matriculas", MatriculaViewSet, basename="Matricula")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("estudantes/<int:pk>/matriculas/", ListaMatriculasEstudanteView.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaMatriculasCursoView.as_view()),
]
