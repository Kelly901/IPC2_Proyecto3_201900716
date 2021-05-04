from django.shortcuts import render, HttpResponse
from .forms import PaginaPrincipal
import requests
#
endpoint= 'http://127.0.0.1:7000/'
# Create your views here.
#Pagina principal 
def index(request):
    reponse=requests.get(endpoint+'mostrarXml')
    variable=reponse.json()
    contexto={
        'variable':variable
    }
    return render(request,'index.html',contexto)

#Mostrar en el area de texto 2
def pagina(request):
    reponse=requests.get(endpoint+'ejemplo')
    variable=reponse.json()
    contexto={
        'variable':variable
    }
    return render(request,'index.html',contexto)

#subir archivo

