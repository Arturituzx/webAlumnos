from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno
from .forms import AlumnoForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def login(request):
    return render(request, 'paginas/login.html')

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/index.html', {'alumnos':alumnos})

def crear(request):
    formulario = AlumnoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('alumnos')
    return render(request, 'alumnos/crear.html', {'formulario':formulario})

def editar(request, id):
    alumnos= Alumno.objects.get(id=id)
    formulario = AlumnoForm(request.POST or None, request.FILES or None, instance = alumnos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('alumnos')
    return render(request, 'alumnos/editar.html', {'formulario':formulario})
def eliminar(request, id):
    alumnos = Alumno.objects.get(id=id)
    alumnos.delete()
    return redirect('alumnos')
def returnImage(request):
    objecto = Alumno.objects.get(id=1)
    rutaImagen = objecto.imagen.url
    return rutaImagen