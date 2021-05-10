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
archivo_xml=""
#Recorrer xml
@app.route("/cargar",methods=['POST'])
def archivo():
    content_dict=xmltodict.parse(request.data)
    print(content_dict["EVENTO"])
    return content_dict
    
#Metodo para cargar Archivo
@app.route("/cargarArchivo",methods=['POST'])
def cargarArchivo():
    print("Hola")
    archivo=request.json
    archivo_xml=archivo['contenido']
    cargarA.procesar(archivo['contenido'])
    diccionario={
        'contenido':archivo['contenido'],
        'estadistica':guardar.retornarEstadistica()
    }
    #print(archivo['contenido'])
    print(diccionario['contenido'])
  
    return jsonify(diccionario)

#
@app.route("/mostrarXml",methods=['GET'])
def mostrarXml():
    
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
        cadena+="\t\tUsuaios afectados:"
        for corr in d.correos:
            cadena+=corr+","
        cadena+="\n"
        cadena+="\t\tError: "+d.codigo+"\n"
        cadena+="\t</EVENTO\n>"
        #Etiquetas del xml
        evento=ET.SubElement(root,"EVENTO")
        fecha="\n\t\tGuatemala, "+d.fecha+"\n"
        correo="\t\tReportado por: "+d.correo+"\n"
        usuarios="\t\tUsuaios afectados:"
        
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
    
    estadist={
        'datos':guardar.mostrarEntrada(),
        'estadistica':guardar.retornarEstadistica()
    }
    return jsonify(estadist)
#
#Retornar Fechas
@app.route("/fecha",methods=['GET'])
def retornarFecha():
    print("fecha")
    fecha={
        'fecha':guardar.fecha()
    }
    print(fecha)
    return jsonify(fecha)
#
@app.route("/opcion",methods=['POST'])
def opciones():
    archivo=request.json
    respuesta={
        'valor':archivo['dato']
    }
    listaU=[]
    listaU2=[]
    #
    total_correos=0
    for i in guardar.datos:
        if i.fecha==respuesta['valor']:
            listaU.append(i.correo)
            total_correos+=1
    #
    for k in listaU:
        if k not in listaU2:
            listaU2.append(k)    
    #   
    cantidad_mensaje=[]
    for h in listaU2:
               
               
        contador=0
        for d in listaU:

            if h==d:
                contador+=1
        print(contador)  
        cantidad_mensaje.append(contador)
    print(cantidad_mensaje)  
    porcentaje=[]
    porc=0
    for c in cantidad_mensaje:
        porc=(c*100)/total_correos
        aproximado=round(porc,2)
        porcentaje.append(str(aproximado))
        print(porcentaje)
    
    lista_completa=[]
   
    informacion={
        'usuarios':listaU2,
        'porcentaje':porcentaje,
        'fecha':respuesta['valor']
    }
    return jsonify(informacion)
# 
@app.route("/opcionError",methods=['POST'])
def opcionError():
    archivo=request.json
    respuesta={
        'valor':archivo['dato']
    }
    listaU=[]
    listaU2=[]
    #
    total_error=0
    for i in guardar.datos:
        if i.fecha==respuesta['valor']:
            listaU.append(i.codigo)
            total_error+=1
    #
    for k in listaU:
        if k not in listaU2:
            listaU2.append(k)    
    #   
    cantidad_mensaje=[]
    for h in listaU2:
               
               
        contador=0
        for d in listaU:

            if h==d:
                contador+=1
        print(contador)  
        cantidad_mensaje.append(contador)
    print(cantidad_mensaje)  
    porcentaje=[]
    porc=0
    for c in cantidad_mensaje:
        porc=(c*100)/total_error
        aproximado=round(porc,2)
        porcentaje.append(str(aproximado))
        print(porcentaje)
    
   
   
    informacion={
        'error':listaU2,
        'porcentaje':porcentaje,
        'fecha':respuesta['valor']
    }
    return jsonify(informacion)

#vaciar el arreglo de objetos
@app.route("/resetear",methods=['GET'])
def resetear():
    guardar.datos.clear()
    mensaje={
        'mensaeje':'Estado actual de la base datos: Vacia'
    }
    return jsonify(mensaje)
    
#      
@app.route("/")
def index():
    return "En linea"
 
if __name__=="__main__":
    app.run(threaded=True,port=7000,debug=True)