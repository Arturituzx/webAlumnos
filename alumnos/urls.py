from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('alumnos', views.alumnos, name='alumnos'),
    path('alumnos/crear', views.crear, name='crear'),
    path('alumnos/editar', views.editar, name='editar')
]