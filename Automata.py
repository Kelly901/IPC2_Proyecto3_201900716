
class Automata:

    def automata(self, lista):
        pos = 0
        estado = 0
        tamaño = len(lista)
        error = ""
        cadena1 = ""

        while pos < tamaño:
            if estado == 0:
                if lista[pos] == "<EVENTOS>":
                    estado = 1
                    pos += 1
                else:
                    error += lista[pos]
                    pos += 1
            elif estado == 1:
                if lista[pos] !="\t<EVENTO>" and lista[pos] != "\t</EVENTO>":
                    estado = 2
                    cadena1 += lista[pos]+"$"
                    pos += 1
                else:
                    error += lista[pos]
                    pos += 1
            elif estado == 2:
                if lista[pos] != "\t</EVENTO>":
                    cadena1 += lista[pos]
                    pos += 1
                elif lista[pos] == "\t</EVENTO>":
                    estado = 1
                    cadena1 += "\n"
                    pos += 1
                else:
                    pos += 1
            elif estado == 3:
                if lista[pos] == "/<EVENTO>":

                    estado = 4
                    pos += 1
                else:
                    cadena1 += lita[pos]
                    error += i
            elif estado == 4:
                pos += 1
            else:
                error+=","
        #print(cadena1)
        return cadena1

    def devolverNombre(self,cadena):
        #cadena="\"Nombre Empleado 1\" xx@ing.usac.edu.gt"
        c1 = ""
        tamaño = len(cadena)
        estado = 0
        error = ""
        cadena2 = ""
        i = 0
        caracter = ""
        while i<tamaño:
   
            if estado==0:
        
                if cadena[i]=="\"":
                    estado=1
                    i+=1
                else:
                    error+=cadena[i]
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

        print(cadena2)
