
from tkinter import messagebox
from servicio import *
from Mensaje import *

class Gestor():
    def ConexionBBDD():
        try:
            Servicio.ConexionBBDD()
            messagebox.showinfo("Conexion",Mensaje.EXITO_BD)
        except:
            messagebox.showinfo("Conexion",Mensaje.ERROR_BD)
    def Eliminar_BBDD():
        if messagebox.askyesno(message=Mensaje.CONFIRMAR_BD, title="Advertencia"):
            Servicio.EliminarBBDD()
        else:
            messagebox.showinfo("Conexion",Mensaje.ERROR_ELIMINAR_DB)
    def Imprimir_BBDD():
        if messagebox.askyesno(message=Mensaje.IMPRIMIR_BD, title="Advertencia"):
            #Servicio.EliminarBBDD()
            messagebox.showinfo("Conexion","Impresion Bd")
    def Mostrar(tree):
        registros=tree.get_children()
        ''' Se puede Abreviar Utilizando otra instruccion
        for elemento in registros:
		    tree.delete(elemento)
        '''
        [tree.delete(elemento) for elemento in registros]
        try:
            empleados = Servicio.Consultar()
            [tree.insert("",0,text=row[0], values=(row[1],row[2],row[3])) for row in empleados]
        except:
            messagebox.showwarning("Advertencia",Mensaje.ERROR_MOSTRAR)
    def Buscar(tree,criterio):
        registros=tree.get_children()
        [tree.delete(elemento) for elemento in registros]
        try:
            if(criterio!=""):
                empleados = Servicio.buscar(criterio)
                [tree.insert("",0,text=row[0], values=(row[1],row[2],row[3])) for row in empleados]
            else:
                messagebox.showwarning("Advertencia",Mensaje.NOMBRE_FALTANTE)
        except:
            messagebox.showwarning("Advertencia",Mensaje.ERROR_BUSCAR)
    def Crear(nombre,cargo,salario):
        try:
            if(nombre!="" and cargo!="" and salario!=""):
                Servicio.crear(nombre,cargo,salario)
            else:
                messagebox.showwarning("Advertencia",Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("Advertencia",Mensaje.ERROR_CREAR)
    def Actualizar(nombre,cargo,salario,ide):
        try:
            if(nombre!="" and cargo!="" and salario!=""):
                Servicio.actualizar(nombre,cargo,salario,ide)
            else:
                messagebox.showwarning("Advertencia",Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("Advertencia",Mensaje.ERROR_ACTUALIZAR)
    def Borrar(ide):
        if messagebox.askyesno(message=Mensaje.CONFIRMAR, title="Advertencia"):
            Servicio.borrar(ide)
        else:
            messagebox.showwarning("Advertencia",Mensaje.ERROR_ELIMINAR)
    def Acerca():
        messagebox.showinfo("Informacion",Mensaje.ACERCA)
    


        