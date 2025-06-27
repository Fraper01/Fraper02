from tkinter import Misc, Tk, Frame, Button, Label, Entry, messagebox, Scrollbar, LabelFrame, Toplevel
from tkinter import ttk, StringVar
from typing import Any, Literal
import sqlite3
import os

class Product:
    db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
    db_name = db_path+"database.db"
    def __init__(self,window) -> None:
        self.wind = window
        self.wind.title("Aplicacion Productos")
        self.Create_widgets()
        self.get_products()
        #self.ConexionBBDD()

    def ConexionBBDD(self):
        try:
            with sqlite3.connect(self.db_name) as sqliteConnection:
                db_is_new = not os.path.exists(self.db_name)
                print(self.db_name)
                print(os.path)
                print(db_is_new)
                db_direct = os.getcwd()
                print(db_direct)
                cursor = sqliteConnection.cursor()
                print('DB Init')
                query = 'select sqlite_version();'
                cursor.execute(query)
                result = cursor.fetchall()
                print('SQLite Version is {}'.format(result))
                print(f'Total_Cambios = {sqliteConnection.total_changes}')
                cursor.close()
        except sqlite3.Error as error:
            print('Error occurred - ', error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite Connection closed')

    def run_query(self, query, parameters =()):
        try:
            with sqlite3.connect(self.db_name) as sqliteConnection:
                cursor = sqliteConnection.cursor()
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                sqliteConnection.commit()
                cursor.close()
        except sqlite3.Error as error:
            sqliteConnection.rollback()
            result = ()
            messagebox.showerror(title=self.wind.title(), message=str(error))
        finally:
            if sqliteConnection:
                sqliteConnection.close()
        return result
    
    def get_products(self):
        record = self.tree.get_children()
        for lrow in record:
            self.tree.delete(lrow)
        query = "SELECT * FROM Productos ORDER BY name DESC;"
        db_rows = self.run_query(query=query)
        for lrow in db_rows:
            self.tree.insert("",0, text=lrow[1], values=lrow[2] )
    
    def validacion(self):
        return (len(self.name.get()) != 0 and len(self.price.get()) != 0 and float(self.price.get()) > 0)

    def borra_entry(self):
        self.name.delete(0,"end")
        self.price.delete(0,"end")

    def add_product(self):
        self.mensaje['text'] = ""
        if self.validacion():
            query = "INSERT INTO Productos(Name, Price) VALUES (?,?)"
            param = (self.name.get(), self.price.get())
            self.run_query(query=query, parameters=param)
            self.get_products()
            self.mensaje['text'] = "El Producto {} ha sido Agredado Satisfactoriamente.".format(self.name.get())
        else:
            #messagebox.showwarning(title=self.wind.title(),message="Los Campos Nombre y Precio son Requeridos")
            self.mensaje['text'] = "Los Campos Nombre y Precio son Requeridos."
        self.borra_entry()

    def delete_product(self):
        self.mensaje['text'] = ""
        try:
            self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            self.mensaje['text'] = "Debe Selecionar un Registro Primero"
            return
        name =  self.tree.item(self.tree.selection())["text"]
        query = "DELETE FROM Productos WHERE name =?;"
        self.run_query(query=query, parameters=(name,))
        self.mensaje['text'] = "El Registro {} fue eliminado Satisfactoriamente".format(name)
        self.get_products()
        self.borra_entry()

    def edit_product(self):
        self.mensaje['text'] = ""
        try:
            self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            self.mensaje['text'] = "Debe Selecionar un Registro Primero"
            return
        name =  self.tree.item(self.tree.selection())["text"]
        old_price = self.tree.item(self.tree.selection())["values"][0]
        self.wEdicion = Toplevel()
        self.wEdicion.title = "Editar Productos"
        Label(self.wEdicion,text="Nombre Anterior:").grid(row=0,column=1)
        Entry(self.wEdicion, textvariable=StringVar(self.wEdicion, value=name), state="readonly").grid(row=0,column=2)
        Label(self.wEdicion,text="Nombre Nuevo:").grid(row=1,column=1)
        new_name = Entry(self.wEdicion)
        new_name.grid(row=1,column=2)
        Label(self.wEdicion,text="Precio Anterior:").grid(row=2,column=1)
        Entry(self.wEdicion, textvariable=StringVar(self.wEdicion, value=old_price), state="readonly").grid(row=2,column=2)
        Label(self.wEdicion,text="Precio Nuevo:").grid(row=3,column=1)
        new_price = Entry(self.wEdicion)
        new_price.grid(row=3,column=2)
        lb =Button(self.wEdicion,text="Guarda Producto", command= lambda: self.edit_records(name, new_name.get(), old_price,new_price.get()))
        lb.grid(row=4,column=1,columnspan=2,sticky="e"+"w")

    def edit_records(self, name, new_name, price, new_price):
        query = "UPDATE Productos SET name=?, price=? WHERE name=? and price=?;"
        param = (new_name,new_price,name, price)
        self.run_query(query=query, parameters=param)
        self.wEdicion.destroy()
        self.mensaje['text'] = "Registro {} ha sido Modificado.".format(new_name)
        self.get_products()
        self.borra_entry()

    def Create_widgets(self):
        frame = LabelFrame(self.wind,text="Registra un Nuevo Producto")
        frame.grid(row=0,column=0, columnspan=3, pady=20)
        Label(frame, text="Nombre:",anchor="e").grid(row=1,column=0) # anchor no me esta funcionado quiero alinear a la derecha
        self.name = Entry(frame)
        self.name.grid(row=1,column=1)
        Label(frame, text="Precio:",anchor="e").grid(row=2,column=0)
        self.price = Entry(frame)
        self.price.grid(row=2,column=1)
        Button(frame,text="Salvar Producto", command=self.add_product).grid(row=3,columnspan=2,sticky="e"+"w") # el boton debe ocupar todo el ancho no se como hacerlo
        self.tree = ttk.Treeview(self.wind,height=10,columns=2)
        self.tree.grid(row=4,column=0,columnspan=2)
        self.tree.heading("#0",text="Nombre",anchor="center")
        self.tree.heading("#1",text="Precio",anchor="center")
        self.mensaje = Label(text="",fg="red")
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky="e"+"w")
        Button(self.wind,text="Delete", command=self.delete_product).grid(row=5,column=0,sticky="e"+"w")
        Button(self.wind,text="Editar", command=self.edit_product).grid(row=5,column=1,sticky="e"+"w")
        self.name.focus()
    
if __name__ == "__main__":
    wproducto = Tk()
    app = Product(wproducto)
    wproducto.mainloop()