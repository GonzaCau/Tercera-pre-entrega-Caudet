from django.shortcuts import render
from django.http import HttpResponse
from miApp.models import Profesor, Alumno, Directivo

# Create your views here.
def cargar_profesor(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ap = request.POST.get('ap')
        dni = request.POST.get('dni')
        sueldo = request.POST.get('sueldo')
        
        profesor = Profesor(nombre = nombre , ap = ap , dni = dni , sueldo = sueldo)
        profesor.save()
        return render(request, 'index.html')
    return render(request,'plantillaCargarProfesor.html')

def cargar_alumno(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ap = request.POST.get('ap')
        dni = request.POST.get('dni')
        
        alumno = Alumno(nombre = nombre , ap = ap , dni = dni)
        alumno.save()
        return render(request, 'index.html')
        
    
    return render(request, 'plantillaCargarAlumno.html')
    
def cargar_directivo(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ap = request.POST.get('ap')
        dni = request.POST.get('dni')
        adhonoren = request.POST.get('adhonoren', False)
        sueldo = request.POST.get('sueldo')
        
        if adhonoren=='on':
            adhonoren=True
        
        directivo = Directivo(nombre = nombre , ap = ap , dni = dni , adhonoren = adhonoren , sueldo = sueldo)
        directivo.save()
        return render(request, 'index.html')
    return render(request, 'plantillaCargarDirectivo.html')

#def ver_profesor(request):
    
    return render(request, 'plantillaVerProfesor.html')

def ver_profesor(request):
    return render(request, 'plantillaVerProfesor.html')
def ver_directivo(request):
    return render(request, 'plantillaVerDirectivo.html')

def ver_alumno(request):
    if request.method == 'GET':
        dni = request.GET.get('dni')
        print(f'-------------------------buscando el dni {dni}')
    return render(request, 'plantillaVerAlumno.html')    
    
def buscar_alumno(request):
    if request.method == 'GET':
        dni = request.GET.get('dni')
        
        if dni is None:
            return HttpResponse('-------------------------enviar el dni a buscar')
        
        alumno= Alumno.objects.filter(dni__iconins=dni)
        print(alumno)
        contexto = {
            'alumno':alumno,
            'dni':dni,
        }
        return render(request, 'busqueda.html', contexto)


def index(request):
    return render(request,'index.html')

