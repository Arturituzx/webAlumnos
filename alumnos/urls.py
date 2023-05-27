from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('alumnos', views.alumnos, name='alumnos'),
    path('alumnos/crear', views.crear, name='crear'),
    path('alumnos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('alumnos/editar/<int:id>', views.editar, name='editar'),
    path('login', views.login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)