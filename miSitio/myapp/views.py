from django.shortcuts import render, HttpResponse
from .forms import PaginaPrincipal, ArchivoEntrada, Obtener_fecha
import requests
#
endpoint= 'http://127.0.0.1:7000/'
# Create your views here.
#Pagina principal 
mostrar=""
def index(request):
    
    return render(request,'index.html')
#Entrear a html Rpeorte reporte
def reporte(request):
    
    return render(request,'Reporte.html')
#Ayuda
def mostrarAyuda(request):

    return render(request,'Ayuda.html')
#Mostrar datos del xml en el area de texto 1
def pagina2(request):
    reponse=requests.get(endpoint+'mostrarXml')
    variable=reponse.json()
    mostrar=True
    contexto={
        'mostrar':mostrar,
        'variable':variable
    }
    return render(request,'index.html',contexto)
#Mostrar en el area de texto 2
def pagina(request):
    reponse=requests.get(endpoint+'estadistica')
    variable=reponse.json()
    mostrar=False
    contexto={
        'datos':variable,
        'variable':variable
    }
    print(contexto)
    return render(request,'index.html',contexto)

#subir archivo

def recibir(request):
    if request.method=='POST':
        ruta=request.POST
        pload=request.POST
        r=request.post(endpoint+'mostrarXml',data=pload)


def cargarArchivo(request):

    contexto={'content':'','response':''}
    print("hola")
    if request.method=='POST':
        form =ArchivoEntrada(request.POST, request.FILES)
        
        print("hola2")
        if form.is_valid():
            filename=request.FILES['file']
            print(filename)
            ruta='C:\\Users\\Kelly\\Downloads\\'
            ruta=ruta+filename.name
            ruta1=r''+ruta
           
            fil=open(ruta1, encoding="utf8")
            contenido=fil.read()
            enviar={
                'contenido':contenido
            }
            response = requests.post(endpoint+'cargarArchivo',json=enviar)
            #contenido=filename.read()
            print(contenido)

            contexto={
                'content':contenido,
                'response':response
            }
            print(contexto['response'])
        else:
            print('Archivo no valido')
        
    return render(request,'index.html',contexto)
    
    #Prueba
def probando(request):
    contexto={
        'dato':""
    }
    if request.method=='GET':
        form =Obtener_fecha(request.GET)
        if form.is_valid():

            opciones=request.GET['opcion']
            print(opciones)
            diccionario={
                'dato':opciones
            }

            reponse=requests.post(endpoint+'opcion',json=diccionario)
            #print("###",reponse.json())
            contexto={'dato':reponse.json()}
    print(contexto)       
    return render(request,'Reporte.html',contexto)

#Filtra por error opcionError
def filtro2(request):
    contexto={
        'dato':""
    }
    if request.method=='GET':
        form =Obtener_fecha(request.GET)
        if form.is_valid():

            opciones=request.GET['opcion']
            print(opciones)
            diccionario={
                'dato':opciones
            }

            reponse=requests.post(endpoint+'opcionError',json=diccionario)
            #print("###",reponse.json())
            contexto={'dato':reponse.json()}
    print(contexto)       
    return render(request,'Reporte.html',contexto)

#Retornar la fecha

def retornar_fechas(request):
    response=requests.get(endpoint+'fecha')
    fechas=response.json()
    
    contexto={
        'fecha':fechas
    }
    return render(request,'Reporte.html',contexto )

def mostrar_informacion(request):
    contexto={
        'mensaje':'mensaje'
    }
    return render(request,'Ayuda.html',contexto )

def vaciar_lista(request):
    response=requests.get(endpoint+'resetear')
    mensaje=response.json()
    diccionario={
        'mensaje':mensaje
    }
    return render(request, 'index.html',diccionario)
#C:\Users\Kelly\Downloads\entrada1.xml
