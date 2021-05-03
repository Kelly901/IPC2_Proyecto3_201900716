
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
            print("\n\n")   



                    