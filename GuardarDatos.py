
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
