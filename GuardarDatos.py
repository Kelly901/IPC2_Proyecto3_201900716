
from Datos import Datos
class GuardarDatos:
    datos=[]
    def guardarDatos(self,fecha,correo,lista,codigo,descripcion):
        d=Datos(fecha, correo, codigo, descripcion)
        self.datos.append(d)
        d.correos=lista
        #for i in lista:
            #d.correos.append(i)


    def imprimir(self):

        for i in self.datos:
            print(">>>>>>>Datos del XML<<<<<<<<<<< ")
            print("Fecha: ",i.fecha)
            print("Correo empleado: ",i.correo)
            print("Correos afectados:  ",i.correos)
            print("Codigo:  ",i.codigo)
            print("Descripcion  ",i.descripcion)
            print("____________")


    def comparar(self):
        fechas=[]
        fecha=[]
        for i in self.datos:
            
            fechas.append(i.fecha)
        print(fechas)    

        for j in fechas:
            if j  not in fecha: 
                fecha.append(j)
        print(fecha)
       
        for i in fecha:
            print(">>>>Fecha "+i+"<<<<<<<<<\n")
            listaU=[]
            listaU2=[]
            for j in self.datos:
                if i==j.fecha:
                    listaU.append(j.correo)
                
            for k in listaU:
              
                if k not in listaU2:
                    listaU2.append(k)
                   
                        

            print(listaU)        
            print(listaU2)

            for h in listaU2:
                cont=0
                for d in listaU:
                    if h==d:
                        cont+=1
                print(cont)
            '''for d in self.datos:
                
                if i==d.fecha:
                    
                    for lis in listaU2:
                        contador=0
                        if lis==d.correo:
                            print(lis)
                            contador+=1
                        print(contador)  '''          
                    #print("Correo del empleado:",j.correo)
        #Recorrer los usuarios afectados
            listaA=[]
            listaA2=[]
            for j in GuardarDatos.datos:
                if i==j.fecha:
                    for recorrer in j.correos:
                        listaA.append(recorrer)
           
                
            for k in listaA:
              
                if k not in listaA2:
                    listaA2.append(k)
            for liss in listaA2:
                print("AFectado: ",liss)
            print("\n\n")   

    def mostrarEntrada(self):
        cadena="<EVENTOS>\n"
    
        for d in self.datos:
            fecha=""
            correo=""
            usuarios=""
            error=""
        #Cdena
            cadena+="\t<EVENTO>\n"
            cadena+="\n\t\tGuatemala, "+d.fecha+"\n"
            cadena+="\t\tReportado por: "+d.correo+"\n"
            cadena+="\t\tUsuaios afectados"
            for corr in d.correos:
                cadena+=corr+","
            cadena+="\n"
            cadena+="\t\tError: "+d.codigo+"\n"
            cadena+="\t</EVENTO>\n"
        #Etiquetas del xml
            
            fecha="\n\t\tGuatemala, "+d.fecha+"\n"
            correo="\t\tReportado por: "+d.correo+"\n"
            usuarios="\t\tUsuarios afectados\n"
            error="\t\tError: "+d.codigo+"\n"
        
            
        cadena+="</EVENTOS>"         
        return cadena       

    #Estadisitcia              
    def retornarEstadistica(self):
        
    
        cadena=""
        cadena="<ESTADISTICAS>\n"
    #--------
        fechas=[]
        fecha=[]
        for i in self.datos:
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
           
            #Etiqueta de Fecha
        
         
          
            cadena+="\t\t<FECHA>"+i+"</FECHA>\n"
        
            #print(">>>>Fecha "+i+"<<<<<<<<<\n")
        
            for j in GuardarDatos.datos:
                if i==j.fecha:
                    cont+=1
                    listaU.append(j.correo)
                    listaR.append(j.codigo)
                
                           
            #Etiqueta de cantidad de mensajes  
        # 
             
           
            
            cadena+="\t\t<CANTIDAD_MENSAJES>"+str(cont)+"</CANTIDAD_MENSAJES>\n" 
            #Etiqueta de reportado por
            cadena+="\t\t<REPORTADO_POR>\n"
            
            #Recorrer la lista con los usurios para agregar a la otra lista de modo que no se repitan 
            for k in listaU:
              
                if k not in listaU2:
                    listaU2.append(k)
            #Recorrer la lista para llenar las etiquetas con los datos
            for h in listaU2:
                #Etiqueta usuario
                cadena+="\t\t\t<USUARIO>\n"
               
                #Etiqueta Email del usuario
                cadena+="\t\t\t"+"\t<EMAIL>"+h+"</EMAIL>\n"
               
               
                contador=0
                for d in listaU:

                    if h==d:
                        contador+=1
                print(contador) 
                #Etiqueta cantidad de mensajes reportados por el usuario
            
          
             
                cadena+="\t\t\t\t<CANTIDAD_MENSAJES>"+str(contador)+"</CANTIDAD_MENSAJES>\n"
           
                cadena+="\t\t\t</USUARIO>\n"
            #Afectados
           
            cadena+="\t\t<AFECTADOS>\n"
            listaA=[]
            listaA2=[]
            for j in self.datos:
                if i==j.fecha:
                
               
                    for recorrer in j.correos:

                        listaA.append(recorrer)
                     
            cadena+="\t\t</AFECTADOS>\n"     
            for k in listaA:
              
                if k not in listaA2:
                    listaA2.append(k)

            for liss in listaA2:  
                        
                cadena+="\t\t\t<AFECTADO>"+liss+"</AFECTADO>\n"
                
            cadena+="\t\t</AFECTADOS>\n" 
            #Errores
            for k in listaR:
              
                if k not in listaR2:
                    listaR2.append(k) 
            #Recorrer las listas con los errores
            cadena+="\t\t<ERRORES>\n"
          
            for h in listaR2:
                #Etiqueta usuario
                cadena+="\t\t\t<ERROR>"+h+"</ERROR>\n"
                #Etiqueta Email del usuario
                
                contador=0
                for d in listaR:
                    if h==d:
                        contador+=1
                #print(contador) 
            #
            
                #Etiqueta cantidad de mensajes reportados por el usuario
                
                cadena+="\t\t\t<CANTIDAD_MENSAJES>"
                cadena+=str(contador)
                cadena+="<CANTIDAD_MENSAJES>\n"
            cadena+="\t\t</ERRORES>\n"     
            cadena+="\t</ESTADISTICA>\n"  
        cadena+="</ESTADISTICAS>\n"    

     
        return cadena
#Fechas
    def fecha(self):
 
    #--------
        fechas=[]
        fecha=[]
        for i in self.datos:
            fechas.append(i.fecha)
            #print(fechas)    

        for j in fechas:
            if j  not in fecha: 
                fecha.append(j)
        #print(fecha)
        return fecha