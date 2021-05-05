from flask import Flask, request, jsonify
from flask_cors import CORS
import xml.etree.ElementTree as ET
import xmltodict
from CargarArchivo import CargarArchivo
from GuardarDatos import GuardarDatos
app=Flask(__name__)
CORS(app)

cargarA=CargarArchivo()
guardar=GuardarDatos()
#Recorrer xml
@app.route("/cargar",methods=['POST'])
def archivo():
    content_dict=xmltodict.parse(request.data)
    print(content_dict["EVENTO"])
    return content_dict
    
#
@app.route("/mostrarXml",methods=['GET'])
def mostrarXml():
    cargarA.procesar()
    root=ET.Element("EVENTOS")
    
    cadena="<EVENTOS>\n"
    
    for d in GuardarDatos.datos:
        fecha=""
        correo=""
        usuarios=""
        error=""
        #Cdena
        cadena+="\t<EVENTO>"
        cadena+="\n\t\tGuatemala, "+d.fecha+"\n"
        cadena+="\t\tReportado por: "+d.correo+"\n"
        cadena+="\t\tUsuaios afectados\n"
        cadena+="\t\tError: "+d.codigo+"\n"
        cadena+="\t</EVENTO>"
        #Etiquetas del xml
        evento=ET.SubElement(root,"EVENTO")
        fecha="\n\t\tGuatemala, "+d.fecha+"\n"
        correo="\t\tReportado por: "+d.correo+"\n"
        usuarios="\t\tUsuaios afectados\n"
        error="\t\tError: "+d.codigo+"\n"
        
        evento.text=fecha+correo+usuarios+error
    cadena+="</EVENTOS>"    
    #print(cadena)
    app.response_class(ET.tostring(root),mimetype='aplication/xml')
    
    archivoXml={
        'archivo': cadena
    }
    return jsonify(archivoXml)

#Estadistica
@app.route("/estadistica",methods=['GET'])
def mostrarEstadistica():
    root=ET.Element("ESTADISTICAS")
    
    cadena=""
    cadena="<ESTADISTICAS>\n"
    #--------
    fechas=[]
    fecha=[]
    for i in GuardarDatos.datos:
        fechas.append(i.fecha)
        #print(fechas)    

    for j in fechas:
        if j  not in fecha: 
            fecha.append(j)
        #print(fecha)
    for i in fecha:
        #Lista para usuarios
        listaU=[]
        listaU2=[]
        #Listas de errores
        listaR=[]
        listaR2=[]
        #Contador de mensajes
        cont=0
        #Etqiueta de Estadistica
        cadena+="\t<ESTADISTICA>\n"
        estadistica=ET.SubElement(root,"ESTADISTICA")
        #Etiqueta de Fecha
        
        etiquetaF=ET.SubElement(estadistica,"FECHA") 
        etiquetaF.text=i
        cadena+="\t\t<FECHA>"+i+"</FECHA>\n"
        
        #print(">>>>Fecha "+i+"<<<<<<<<<\n")
        
        for j in GuardarDatos.datos:
            if i==j.fecha:
                cont+=1
                listaU.append(j.correo)
                listaR.append(j.codigo)
                
                           
        #Etiqueta de cantidad de mensajes  
        # 
             
        etiquetM=ET.SubElement(estadistica,"CANTIDAD_MENSAJES")
        etiquetM.text=str(cont)
        cadena+="\t\t<CANTIDAD_MENSAJES>"+str(cont)+"</CANTIDAD_MENSAJES>\n" 
        #Etiqueta de reportado por
        cadena+="\t\t<REPORTADO_POR>\n"
        etiquetaRepor=ET.SubElement(estadistica,"REPORTADO_POR")
        #Recorrer la lista con los usurios para agregar a la otra lista de modo que no se repitan 
        for k in listaU:
              
            if k not in listaU2:
                listaU2.append(k)
        #Recorrer la lista para llenar las etiquetas con los datos
        for h in listaU2:
            #Etiqueta usuario
            cadena+="\t\t\t<USUARIO>\n"
            etiquetaU=ET.SubElement(etiquetaRepor,"USUARIO") 
            #Etiqueta Email del usuario
            cadena+="\t\t\t"+"\t<EMAIL>"+h+"</EMAIL>\n"
            etiquetaEmail=ET.SubElement(etiquetaU,"EMAIL")
            etiquetaEmail.text=h
            contador=0
            for d in listaU:

                if h==d:
                    contador+=1
            print(contador) 
            #Etiqueta cantidad de mensajes reportados por el usuario
            
            etiquetaMens=ET.SubElement(etiquetaU,"CANTIDAD_MENSAJES")
            etiquetaMens.text=str(contador)
            cadena+="\t\t\t\t<CANTIDAD_MENSAJES>"+str(contador)+"</CANTIDAD_MENSAJES>\n"
           
            cadena+="\t\t\t</USUARIO>\n"
        #Afectados
        etiquetaAfec=ET.SubElement(estadistica, "AFECTADOS")
        cadena+="\t\t<AFECTADOS>\n"
        for j in GuardarDatos.datos:
            if i==j.fecha:
                
               
                for recorrer in j.correos:

                    etiquetaAf=ET.SubElement(etiquetaAfec,"AFECTADO")
                    cadena+="\t\t\t<AFECTADO>"+recorrer+"</AFECTADO>\n"
                    etiquetaAf.text=recorrer  
        cadena+="\t\t</AFECTADOS>\n"            
        #Errores
        for k in listaR:
              
            if k not in listaR2:
                listaR2.append(k) 
        #Recorrer las listas con los errores
        cadena+="\t\t<ERRORES>\n"
        etiquetaErr=ET.SubElement(estadistica,"ERRORES")
        for h in listaR2:
            #Etiqueta usuario
            cadena+="\t\t\t<ERROR>"+h+"</ERROR>\n"
            #Etiqueta Email del usuario
            etiquetaError=ET.SubElement(etiquetaErr,"ERROR")
            etiquetaError.text=h
            contador=0
            for d in listaR:
                if h==d:
                    contador+=1
            print(contador) 
            #
            
            #Etiqueta cantidad de mensajes reportados por el usuario
            etiquetaCo=ET.SubElement(etiquetaErr,"CANTIDAD_MENSAJES")
            etiquetaCo.text=str(contador)  
            cadena+="\t\t\t<CANTIDAD_MENSAJES>"
            cadena+=str(contador)
            cadena+="<CANTIDAD_MENSAJES>\n"
        cadena+="\t\t</ERRORES>\n"     
        cadena+="\t</ESTADISTICA>\n"  
    cadena+="</ESTADISTICAS>\n"               
        #print("\n\n")




    #------
    '''for d in GuardarDatos.datos:
        fecha1=""
        correo=""
        usuarios=""
        error=""
        if d.fecha:
           fecha1=d.fecha
           
           correo1=ET.SubElement(estadistica,"USUARIO")
           
           
           correo1.text=d.correo
        evento=ET.SubElement(root,"PENDIENTE")
        fecha="\n\t\tGuatemala, "+d.fecha+"\n"
        correo="\t\tReportado por: "+d.correo+"\n"
        usuarios="\t\tUsuaios afectados\n"
        error="\t\tError: "+d.codigo+"\n"'''
        
        #evento.text=fecha+correo+usuarios+error
        
    #print(cadena)
    #app.response_class(ET.tostring(root),mimetype='aplication/xml')
    estadist={
        'datos':guardar.mostrarEntrada(),
        'estadistica':cadena
    }
    return jsonify(estadist)
#
@app.route("/ejemplo",methods=['GET'])
def ejemplos():
    respuesta={
        'valor':'sale ipc2'
        
    }
    return jsonify(respuesta)
#        
@app.route("/")
def index():
    return "En linea"
 
if __name__=="__main__":
    app.run(threaded=True,port=7000,debug=True)