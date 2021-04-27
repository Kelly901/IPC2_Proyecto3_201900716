import xml.etree.ElementTree as ET
from lxml import etree
import re
import io

class CargarArchivo:

    def procesar(self):
        ruta1=input("ingrese la ruta")
        ruta=r''+ruta1
        fi=open(ruta1,encoding="utf8")
        mensaje=fi.read()
        #print(mensaje)
        
        conversion=re.sub(r'<+@>',r'\1\2',mensaje)
        print(conversion)

        #tree=ET.parse(ruta)
        #root=tree.getroot()
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
        #root=tree.getroot()
        #print(root)
        #for i in root:
            #print(i)
         
        '''with io.open(ruta,'r',encoding='utf-8-sig') as f:
            contents=f.read()
            tree=ET.fromstring(contents)    
            print(tree)'''
        
       
#C:\Users\Kelly\Desktop\[IPC2]Proyecto3\IPC2_Proyecto3_201900716\prueba.xml
#C:\Users\Kelly\Downloads\data.txt
c=CargarArchivo()
c.procesar()
'''parser=ET.XMLParser(encoding="utf-8")
    tree=ET.fromstring(ruta,parser=parser)
    tree=ET.parse(ruta)
    '''