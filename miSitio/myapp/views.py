from django.shortcuts import render, HttpResponse
from .forms import PaginaPrincipal
import requests
#
endpoint= 'http://127.0.0.1:7000/'
# Create your views here.
#Pagina principal 
mostrar=""
def index(request):
    
    return render(request,'index.html')
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


