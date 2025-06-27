# Importar Bibliotecas
from tkinter import *
from tkinter import messagebox, ttk 
from tkinter import font
from gestor import *
from Mensaje import *

def ConexionBBDD():
	Gestor.ConexionBBDD()
def EliminarBBDD():
	Gestor.Eliminar_BBDD()
	MostrarLimpiar()
def ImprimirBBDD():
	Gestor.Imprimir_BBDD()
	MostrarLimpiar()
def MostrarLimpiar():
	LimpiarCampos()
	Mostrar()
def LimpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")
def Mostrar():
	Gestor.Mostrar(tree)
	#menubasedat.entryconfig("Salir", state=NORMAL) deberia funcionar en otro lugar
def salirAplicacion():
	valor=messagebox.askquestion(title="Salir",message=Mensaje.SALIR)
	root.destroy() if valor=="yes" else None
def Crear():
	Gestor.Crear(miNombre.get(),miCargo.get(),miSalario.get())
	MostrarLimpiar()
def Actualizar():
	Gestor.Actualizar(miNombre.get(),miCargo.get(),miSalario.get(), miId.get())
	MostrarLimpiar()
def Borrar():
	Gestor.Borrar(miId.get())
	MostrarLimpiar()
def Buscar():
	Gestor.Buscar(tree, miNombre.get())
def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	miNombre.set(tree.item(item,"values")[0])
	miCargo.set(tree.item(item,"values")[1])
	miSalario.set(tree.item(item,"values")[2])
def MensajeA():
	Gestor.Acerca()
	MostrarLimpiar()
def control_s_presionado(event=None):
    salirAplicacion()

# Desarrollo de la Interfaz grafica
root=Tk()
root.title("Aplicación CRUD con Base de Datos")
root.config(background="lightblue")
root.geometry("600x350")

db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"

imagen_buscar=PhotoImage(file=db_path+"Imagenes/buscar.png") # Esta dentro de tkinter
imagen_crear=PhotoImage(file=db_path+"imagenes/crear.png")
imagen_mostrar=PhotoImage(file=db_path+"imagenes/mostrar.png")
imagen_actualizar=PhotoImage(file=db_path+"imagenes/actualizar.png")
imagen_eliminar=PhotoImage(file=db_path+"imagenes/eliminar.png")

miId=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSalario=StringVar()
db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
db_name = db_path+"base2"

################################## Tabla ################################
cabecera = ["Id","Nombre del Empleado","Cargo","Salario"]
tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.column('#3', width=100)

'''
tree.heading("#0", text=cabecera[0], anchor=CENTER)
tree.heading('#1', text=cabecera[1], anchor=CENTER)
tree.heading('#2', text=cabecera[2], anchor=CENTER)
tree.heading('#3', text=cabecera[3], anchor=CENTER)
'''
[tree.heading("#" + str(cabecera.index(cont)), text=cont, anchor=CENTER) for cont in cabecera]

tree.bind("<Double-1>", seleccionarUsandoClick)
tree.bind("<Button-1>", seleccionarUsandoClick)
MostrarLimpiar()

###################### Colocar widgets en la VISTA ######################
########## Creando Los menus ###############
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=ConexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos", command=EliminarBBDD)
menubasedat.add_command(label="Imprimir Base de Datos", command=ImprimirBBDD)
menubasedat.add_separator()
menubasedat.add_command(label="Salir", command=salirAplicacion, accelerator="Alt+S", image=imagen_buscar, compound=LEFT, state=NORMAL,
						# Tipo de fuente.
    					font=font.Font(family="Times", size=14),
    					# Color de fondo.
						background="#ADD8E6",
						# Color del texto.
						foreground="#FF0000",
						# Color de fondo cuanto el botón tiene el foco.
						activebackground="#32CDFF",
						# Color del texto cuando el botón tiene el foco.
						activeforeground="#FFFF00")
# Asociar el atajo del teclado del menú "Salir".
root.bind_all("<Alt-s>", control_s_presionado)
menubar.add_cascade(label="Inicio", menu=menubasedat)
ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=MostrarLimpiar)
ayudamenu.add_command(label="Acerca", command=MensajeA)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)
############## Creando etiquetas y cajas de texto ###########################
Label(root, text="Nombre", bg="lightblue").place(x=50,y=10)
Label(root, text="Cargo", bg="lightblue").place(x=50,y=40)
Label(root, text="Salario", bg="lightblue").place(x=280,y=40)
Label(root, text="USD", bg="lightblue").place(x=380,y=40)
Entry(root, textvariable=miId)
Entry(root, textvariable=miNombre, width=50).place(x=100, y=10)
Entry(root, textvariable=miCargo).place(x=100, y=40)
Entry(root, textvariable=miSalario, width=10).place(x=320, y=40)
################# Creando botones ###########################
Button(root, text="Crear Registro",image=imagen_crear, command=Crear,bg="green").place(x=50, y=90)
Button(root, text="Modificar Registro",image=imagen_actualizar, command=Actualizar,bg="blue").place(x=180, y=90)
Button(root, text="Mostrar Lista", image=imagen_mostrar,command=MostrarLimpiar,bg="blue").place(x=320, y=90)
Button(root, text="Eliminar Registro",image=imagen_eliminar,bg="red", command=Borrar).place(x=450, y=90)
Button(root, text="Buscar Registro", image=imagen_buscar, command=Buscar,bg="blue").place(x=450, y=10)

root.config(menu=menubar)

root.mainloop()