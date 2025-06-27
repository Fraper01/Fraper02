# Clase de Ciudades
import mysql.connector
from mysql.connector import errorcode
from tkinter import messagebox

class Ciudades():
    def __init__(self) -> None:
        self.cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    def __str__(self) -> str:
        datos = self.consulta_ciudades()
        aux = ""
        for fila in datos:
            aux = aux + str(fila) + "\n"
        return aux
    def consulta_ciudades(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM countries;")
        datos = cur.fetchall()
        cur.close()
        return datos
    def buscar_ciudades(self,aId):
        cur = self.cnn.cursor()
        lsql = "SELECT * FROM countries WHERE ID={};".format(aId)
        cur.execute(lsql)
        datos = cur.fetchone()
        cur.close()
        return datos
    def inserta_ciudadesAt(self,aISO3,aCountryName,aCapital,aCurrencyCode):
        cur = self.cnn.cursor()
        lsql = "INSERT INTO countries(ISO3,CountryName,Capital,CurrencyCode) VALUES('{}','{}','{}','{}');".format(aISO3,aCountryName,aCapital,aCurrencyCode)
        n=0
        try:
            cur.execute(lsql)
        except mysql.connector.Error as e:
            cur.close()
            '''
            showinfo()
            showwarning()
            showerror()
            '''
            messagebox.showerror(title="Bd Error", message=str(e))
            n= -1
        else:
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
        finally:
            return n
    def elimina_ciudades(self,aid):
        cur = self.cnn.cursor()
        lsql = "DELETE FROM countries WHERE ID={};".format(aid)
        cur.execute(lsql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    def modifica_ciudades(self,aid,aISO3='',aCountryName='',aCapital='',aCurrencyCode=''):
        if aISO3=='' and aCountryName=='' and aCapital=='' and aCurrencyCode=='':
            return 0
        lsqlUp = "UPDATE countries "
        lsqlSe = "SET "
        lsqlWh = " WHERE ID={};".format(aid)
        if aISO3!='':
            lsqlSe = lsqlSe + "ISO3 = '{}'".format(aISO3)
        if aCountryName!='':
            if len(lsqlSe)>=5:
                lsqlSe = lsqlSe + ","
            lsqlSe = lsqlSe + "CountryName = '{}'".format(aCountryName) 
        if aCapital!='':
            if len(lsqlSe)>=5:
                lsqlSe = lsqlSe + ","
            lsqlSe = lsqlSe + "Capital = '{}'".format(aCapital) 
        if aCurrencyCode!='':
            if len(lsqlSe)>=5:
                lsqlSe = lsqlSe + ","
            lsqlSe = lsqlSe + "CurrencyCode = '{}'".format(aCurrencyCode) 
        lsql = lsqlUp + lsqlSe + lsqlWh 
        cur = self.cnn.cursor()
        n = 0
        try:
            cur.execute(lsql)
        except mysql.connector.Error as e:
            cur.close()
            '''
            showinfo()
            showwarning()
            showerror()
            '''
            messagebox.showerror(title="Bd Error", message=str(e))
            n= -1
        else:
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
        finally:
            return n

