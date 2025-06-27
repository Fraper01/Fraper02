import sqlite3
from consulta import Consulta
from Empleado import Empleado
from tkinter import messagebox

class Servicio:
    def run_query(query, parameters =(), adb_path="", adb_name="", atupla=0):
        try:
            if adb_path == "":
                db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
            else:
                db_path = adb_path
            if adb_name == "":
                db_name = db_path+"base2"
            else:
                db_name = db_path+adb_name
            with sqlite3.connect(db_name) as sqliteConnection:
                cursor = sqliteConnection.cursor()
                cursor.execute(query, parameters)
                if atupla == 0:
                    result = cursor.fetchall()
                else:
                    result = cursor.fetchone()
                sqliteConnection.commit()
                cursor.close()
        except sqlite3.Error as error:
            sqliteConnection.rollback()
            messagebox.showerror(title="Error", message=str(error))
            result = ()
        finally:
            if sqliteConnection:
                sqliteConnection.close()
        return result
    '''
    def Conectar():
        db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
        db_name = db_path+"base2"
        miconexion = sqlite3.connect(db_name)
        micursor = miconexion.cursor()
        return miconexion, micursor
    def Desconectar(conexion,cursor):
        cursor.close
        if conexion:
            conexion.close()
    def ConexionBBDD():
        miconexion, micursor = Servicio.Conectar()
        li_ret = micursor.execute(Consulta.CREATE)
        Servicio.Desconectar(miconexion,micursor)
        return li_ret
    def EliminarBBDD():
        miconexion, micursor = Servicio.Conectar()
        micursor.execute(Consulta.DELETE_TABLE)
        Servicio.Desconectar(miconexion,micursor)
    '''
    def Consultar():
        return Servicio.run_query(Consulta.SELECT)
        '''
        miconexion, micursor = Servicio.Conectar()
        try:
            micursor.execute(Consulta.SELECT)
            miconexion.commit()
            result = micursor.fetchall()
        except sqlite3.Error as error:
            miconexion.rollback()
            result = ()
            messagebox.showerror(title="Error", message=str(error))
        Servicio.Desconectar(miconexion,micursor)
        '''
        return result
    def crear(nombre,cargo,salario):
        empleado = Empleado(nombre,cargo,salario)
        Servicio.run_query(Consulta.INSERT,empleado.info())
        '''
        miconexion, micursor = Servicio.Conectar()
        empleado = Empleado(nombre,cargo,salario)
        try:
            micursor.execute(Consulta.INSERT,empleado.info())
            miconexion.commit()
            result2 = micursor.lastrowid
            result3 = micursor.rowcount
            result = micursor.fetchall()
        except sqlite3.Error as error:
            miconexion.rollback()
            messagebox.showerror(title="Error", message=str(error))
            result = ()
        Servicio.Desconectar(miconexion,micursor)
        '''
    def actualizar(nombre,cargo,salario, ide):
        empleado = Empleado(nombre,cargo,salario)
        Servicio.run_query(Consulta.UPDATE+ide,empleado.info())
        '''
        miconexion, micursor = Servicio.Conectar()
        empleado = Empleado(nombre,cargo,salario)
        try:
            micursor.execute(Consulta.UPDATE+ide,empleado.info())
            miconexion.commit()
            result = micursor.fetchall()
            result2 = micursor.lastrowid
            result3 = micursor.rowcount
        except sqlite3.Error as error:
            miconexion.rollback()
            messagebox.showerror(title="Error", message=str(error))
            result = ()
        Servicio.Desconectar(miconexion,micursor)
        '''
    def borrar(ide):
        Servicio.run_query(Consulta.DELETE+ide)
        '''
        miconexion, micursor = Servicio.Conectar()
        try:
            micursor.execute(Consulta.DELETE+ide)
            miconexion.commit()
            result = micursor.fetchall()
            result2 = micursor.lastrowid
            result3 = micursor.rowcount
        except sqlite3.Error as error:
            miconexion.rollback()
            messagebox.showerror(title="Error", message=str(error))
            result = ()
        Servicio.Desconectar(miconexion,micursor)
        '''
    def buscar(nombre):
        return Servicio.run_query(Consulta.BUSCAR,(nombre,))
        '''
        miconexion, micursor = Servicio.Conectar()
        try:
            micursor.execute(Consulta.BUSCAR,(nombre,))
            miconexion.commit()
            result = micursor.fetchall()
        except sqlite3.Error as error:
            miconexion.rollback()
            messagebox.showerror(title="Error", message=str(error))
            result = ()
        Servicio.Desconectar(miconexion,micursor)
        return result
        '''
    
    
    


