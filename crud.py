import sqlite3
from tkinter import messagebox, Tk, StringVar, Menu, Entry, Label, Button
from tkinter import ttk
import os

root = Tk()
root.title("Aplicacion Crud con Base de Datos")
root.geometry("600x350")

miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()
db_filename = 'base'

def ConexionBBDD():
    db_filename = 'base'
    db_is_new = not os.path.exists(db_filename)
    db_direct = os.getcwd()

    miConexion = sqlite3.connect(db_filename)
    micursor = miConexion.cursor()
    try:
        schema = '''
        create table empleados(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50) NOT NULL,
            Cargo VARCHAR(50) NOT NULL,
            Salario INT NOT NULL
        );'''
        if db_is_new == True or db_is_new == False:
            micursor.execute(schema)
            messagebox.showinfo("CONEXION","Base de Datos Creada Exitosamente")
        else:
            messagebox.showinfo("CONEXION","Conexion Exitosa con la Base de Datos")
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    micursor.close()
    miConexion.close()

def EliminarBBDD():
    miConexion = sqlite3.connect("base")
    micursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message="Los Datos se perderan definitivamente. Desea Continuar?",title="Advertencia"):
            micursor.execute("DROP TABLE empleados;")
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    micursor.close()
    miConexion.close()

def SalirAplicacion():
    valor = messagebox.askquestion("Salir","Esta Seguro que desea Salir de la Aplicacion?")
    if valor == messagebox.YES:
        root.destroy()

def LimpiarCanpos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def Mensaje():
    acerca = '''
    Aplicacion CRUD
    Version 1.0
    Tecnologia Pyton Tkinter
    '''
    messagebox.showinfo("Informacion",acerca)

def Crear():
    try:
        with sqlite3.connect(db_filename) as miConexion:
            # add a new registro
            sql = ''' INSERT INTO empleados(Nombre,Cargo,Salario)
                      VALUES(?,?,?) '''
            datos=miNombre.get(),miCargo.get(),miSalario.get()
            cur = miConexion.cursor()
            cur.execute(sql, datos)
            miConexion.commit()
            lastrowId = cur.lastrowid
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    else:
        n=cur.rowcount
    finally:
        cur.close()
        miConexion.close()
    LimpiarCanpos()
    Mostrar()

def Mostrar():
    miConexion = sqlite3.connect("base")
    micursor = miConexion.cursor()
    reg = tree.get_children()
    for elemento in reg:
        tree.delete(elemento)
    try:
        micursor.execute("SELECT * FROM empleados ORDER BY ID DESC;")
        for row in micursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    finally:
        micursor.close()
        miConexion.close()

tree = ttk.Treeview(height=10,columns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column("#0",width=100,)
tree.heading("#0",text="ID",anchor="center")
tree.heading("#1",text="Nombre Empleado",anchor="center")
tree.heading("#2",text="Cargo",anchor="center")
tree.column("#3",width=100,)
tree.heading("#3",text="Salario",anchor="e")

def SeleccionarconClick(event):
    item = tree.identify('item',event.x, event.y)
    miId.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miCargo.set(tree.item(item,"values")[1])
    miSalario.set(tree.item(item,"values")[2])
tree.bind("<Double-1>", SeleccionarconClick) # Doble Click
tree.bind("<Button-1>", SeleccionarconClick) # Click

def Actualizar():
    miConexion = sqlite3.connect("base")
    micursor = miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        micursor.execute("UPDATE empleados SET NOMBRE=?,CARGO=?,SALARIO=? WHERE ID="+miId.get(),(datos))
        miConexion.commit()
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    finally:
        micursor.close()
        miConexion.close()
    LimpiarCanpos()
    Mostrar()

def Borrar():
    miConexion = sqlite3.connect("base")
    micursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message="Realmente Desea Eliminar el Registro?",title="Advertencia"):
            micursor.execute("DELETE FROM empleados WHERE ID="+miId.get())
            miConexion.commit()
    except sqlite3.Error as e:
        messagebox.showerror(title="Bd Error", message=str(e))
    finally:
        micursor.close()
        miConexion.close()
    LimpiarCanpos()
    Mostrar()

menubar = Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear Conectar Bd",command=ConexionBBDD)
menubasedat.add_command(label="Eliminar Bd",command=EliminarBBDD)
menubasedat.add_command(label="Salir",command=SalirAplicacion)
menubar.add_cascade(label="Inicio",menu=menubasedat)
ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos",command=LimpiarCanpos)
ayudamenu.add_command(label="Acerca",command=Mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)
root.config(menu=menubar)

e1 = Entry(root, textvariable=miId)
Label(root,text="Nombre:").place(x=40,y=10)
e2 = Entry(root, textvariable=miNombre, width=50).place(x=100,y=10)
Label(root,text="Cargo:").place(x=50,y=40)
e3 = Entry(root, textvariable=miCargo).place(x=100,y=40)
Label(root,text="Salario:").place(x=270,y=40)
e4 = Entry(root, textvariable=miSalario, width=10).place(x=320,y=40)
Label(root,text="USD").place(x=380,y=40)

b1 = Button(root,text="Crear Registro", command=Crear).place(x=50,y=90)
b2 = Button(root,text="Modificar Registro", command=Actualizar).place(x=180,y=90)
b3 = Button(root,text="Mostar Lista", command=Mostrar).place(x=320,y=90)
b4 = Button(root,text="Eliminar Registro", bg="red",command=Borrar).place(x=450,y=90)


root.mainloop()


