import re
cadena="\"Nombre Empleado 1\" xx@ing.usac.edu.gt"
c1=""
tamaño=len(cadena)
estado=0
error=""
cadena2=""
i=0
caracter=""
'''while i<tamaño:
   
    if estado==0:
        
        if cadena[i]=="\"":
            estado=1
            i+=1
        else:
            erro+=cadena[i]
            i+=1
    elif estado==1:
        if cadena[i]!="\"":
            cadena2+=cadena[i]
            i+=1

        elif cadena[i]=="\"":
            i+=1
            estado=2
        else:
            i+=1  
                        
    elif estado==2:

        i+=1
    else:
        print("")    

print(cadena2)'''

cadena="3/12/20231 mdm"

patron=re.compile("[0-3]\d/[0-1]\d/\d+")
fecha=re.search(patron, cadena)

#print(fecha.group())
cadena3="Error:   213333 -La computadora esta superererere lenta viera"    
patron2=re.compile("-\s+\w[\w\s]+|-\w[\w\s]+")
descripcion=patron2.search(cadena3)
des2=descripcion.group()
descripcion1=re.search(r'[\w]+[\s\w]+', des2)
descrip=descripcion1.group()
print(descrip)



lista3=[]
lista4=[1,2,3,4,4,5]
lista3=lista4
print(lista3)


