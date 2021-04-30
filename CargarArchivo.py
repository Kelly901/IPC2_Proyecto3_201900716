import xml.etree.ElementTree as ET
from lxml import etree
from Automata import Automata
from GuardarDatos import GuardarDatos
import re
import io
auto = Automata()
guardar=GuardarDatos()

class CargarArchivo:

    def procesar(self):
        ruta1 = input("ingrese la ruta")
        ruta = r''+ruta1
        fi = open(ruta1, encoding="utf8")
        mensaje = fi.read()

        lista = mensaje.split("\n")
        # print(lista)
        #
        texto = auto.automata(lista)
        print(texto)
        eventos = texto.split("\n")

        #Patron para la fecha
        patronF=re.compile(r'[0-3]\d/[0-1]\d/\d+')
        #Patron para el correo
        patronN=re.compile(r'\w+@[\w\.\w]+')
        #Patron para codigo de error
        patronE=re.compile(r'\d+')
        #Patron de descripción
        patronD=re.compile(":\s+\w[\w\s]+")

        

        for i in range(0,len(eventos)-1):
            print("__________________________")

            lista2 = eventos[i].split("$")
            #Fecha
            fecha=patronF.search(lista2[0])
            #Correo del empleado 
            correo1=patronN.search(lista2[1])
            print(lista2[1])
            print(fecha.group())
            print(correo1.group())
            #Correo de los afectados
            correosAfectados=patronN.findall(lista2[2])
            print(correosAfectados)
            #Codigo del error
            error=patronE.search(lista2[3])
            print(error.group())
            #Descripcion
            cadenaTemp=patronD.findall(lista2[3])
            descrip=""
            descripcion=re.search(r'[\w]+[\s\w]+', cadenaTemp[1])
            descrip=descripcion.group()
            #print(descripcion.group())
            for j in range(4,len(lista2)-1):
                #print(lista2[j])    
                descrip+="\n"+lista2[j]          
            print(descrip)
            guardar.guardarDatos(fecha.group(), correo1.group(),correosAfectados,error.group(), descrip)
        
        #Imprimir
        guardar.imprimir()
        
        
        
        '''for i in lista:
            if i!="<EVENTO>" and i!="<EVENTOS>" and i!="</EVENTO>" and i!="</EVENTOS>":
                print(i)'''
        
        #
        '''tree=ET.parse(ruta)
        tree.decode(encoding='UTF-8',errors='strict')'''
        '''parser=etree.XMLParser(recover=True)
        tree=etree.fromstring(ruta,parser=parser)
        print(tree)
        cadena=etree.parse(ruta)
        xmlString=etree.toString(cadena,encoding='utf-8',method='xml')
        print(xmlString)'''

        #
        '''parser=ET.XMLParser(encoding="utf-8")
        parse=re.sub(r'<>',parser)
        tree=ET.fromstring(ruta,parser=parser)
        root=tree.getroot()'''
        '''parser=ET.XMLParser(encoding='utf-8')
        print(parser)
        tree=ET.fromstring(ruta,parser=parser)
        print(tree)'''
        # root=tree.getroot()
        # print(root)
        # for i in root:
        # print(i)

        '''with io.open(ruta,'r',encoding='utf-8-sig') as f:
            contents=f.read()
            tree=ET.fromstring(contents)    
            print(tree)'''

#\w+\@[\w\.\w]+
# C:\Users\Kelly\Desktop\[IPC2]Proyecto3\IPC2_Proyecto3_201900716\prueba.xml
# C:\Users\Kelly\Desktop\[IPC2]Proyecto3\IPC2_Proyecto3_201900716\prueba2.xml
# C:\Users\Kelly\Downloads\data.txt
# C:\Users\Kelly\Downloads\entrada.xml
c = CargarArchivo()
c.procesar()
'''parser=ET.XMLParser(encoding="utf-8")
    tree=ET.fromstring(ruta,parser=parser)
    tree=ET.parse(ruta)
    '''
