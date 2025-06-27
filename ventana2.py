# Ejemplo Ventana de Fraciones Mixtas

from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Text, IntVar, Radiobutton, Scrollbar
from clases3 import FraccionMixta
from tkinter.ttk import Combobox # Dentro de tkinter.ttk esta los widgets tematicos

class MainFrame(Frame):
    def __init__(self, master=None):
        #super().__init__(master, width=320, height=170, bg="green")
        super().__init__(master, width=320, height=320, bg="#F1F8EC") # En Exdecimal el color
        '''
        self ahora es mi Frame principal que esta en toda la ventana
        '''
        self.master = master
        self.pack()
        '''
        para crear un variable general de la clase se crea aqui en el constructor
        '''
        self.var_op = IntVar() # Declara un tipo de Variable Entera
        self.create_widgets()
    def fcalcular(self):
        lb_res = False
        ent1 = int(self.txt1E.get())
        num1 = int(self.txt1N.get())
        den1 = int(self.txt1D.get())
        fra1 = FraccionMixta(ent1,num1,den1)
        ent2 = int(self.txt2E.get())
        num2 = int(self.txt2N.get())
        den2 = int(self.txt2D.get())
        fra2 = FraccionMixta(ent2,num2,den2)
        #print(self.cbopciones.current()) # Indica el indice seleccionado
        #print(self.cbopciones.get()) # Indica el texto del seleccionda
        if self.cbopciones.get() == self.opciones[0]: # Suma
            fras = fra1 + fra2
            lb_res = True
        elif self.cbopciones.get() == self.opciones[1]: # Resta
            fras = fra1 - fra2
            lb_res = True
        elif self.cbopciones.get() == self.opciones[2]: # Multiuplicacion
            fras = fra1 * fra2
            lb_res = True
        elif self.cbopciones.get() == self.opciones[3]: # Division
            fras = fra1 / fra2
            lb_res = True
        elif self.cbopciones.get() == self.opciones[4]: # son Iguales
            if fra1 == fra2:
                messagebox.showinfo(title=self.winfo_parent(), message="Las Fracciones son Iguales")
            else:
                messagebox.showinfo(title=self.winfo_parent(), message="Las Fracciones son diferentes")
        else:
            fras = fra1 + fra2
            lb_res = True
            
        if lb_res:
            #self.txtres.delete(0,"end") # Esto limpia los controles Entry
            #self.txtres.delete(1.0,"end") # Esto limpia los controles Texto
            #self.txtres.insert(0,fras) # Esto funciona para el control Entry
            self.txtres.insert(1.0,fras) # Esto funciona para el control Texto
            self.txtres.insert('current', '\n') # Adiciona en la posicion actual los textos trabajan como una matriz fila.columna en index devuelve su posicion
            #self.txtres.insert('end', '\n') # Adiciona al final del texto
            #self.txtres.insert('insert', '\n') # Adiciona al final del texto o donde el quiera no se

    def fcalcular2(self):
        lb_res = False
        ent1 = int(self.txt1E.get())
        num1 = int(self.txt1N.get())
        den1 = int(self.txt1D.get())
        fra1 = FraccionMixta(ent1,num1,den1)
        ent2 = int(self.txt2E.get())
        num2 = int(self.txt2N.get())
        den2 = int(self.txt2D.get())
        fra2 = FraccionMixta(ent2,num2,den2)
        if self.var_op.get() == 0: # Suma
            fras = fra1 + fra2
            lb_res = True
        elif self.var_op.get() == 1: # Resta
            fras = fra1 - fra2
            lb_res = True
        elif self.var_op.get() == 2: # Multiuplicacion
            fras = fra1 * fra2
            lb_res = True
        elif self.var_op.get() == 3: # Division
            fras = fra1 / fra2
            lb_res = True
        elif self.var_op.get() == 4: # son Iguales
            if fra1 == fra2:
                messagebox.showinfo(title=self.winfo_parent(), message="Las Fracciones son Iguales")
            else:
                messagebox.showinfo(title=self.winfo_parent(), message="Las Fracciones son diferentes")
        else:
            fras = fra1 + fra2
            lb_res = True
            
        if lb_res:
            #self.txtres.delete(0,"end") # Esto limpia los controles Entry
            #self.txtres.delete(1.0,"end") # Esto limpia los controles Texto
            #self.txtres.insert(0,fras) # Esto funciona para el control Entry
            self.txtres.insert(1.0,fras) # Esto funciona para el control Texto
            self.txtres.insert('current', '\n') # Adiciona en la posicion actual los textos trabajan como una matriz fila.columna en index devuelve su posicion
            #self.txtres.insert('end', '\n') # Adiciona al final del texto
            #self.txtres.insert('insert', '\n') # Adiciona al final del texto o donde el quiera no se

    def create_widgets(self):
        frame_funo = Frame(self, width=100, height=60, bg="#FFFFCD")
        frame_funo.place(x=30,y=40)
        frame_x1 = Frame(frame_funo,width=42,height=27, bg="#A7E8FF")
        frame_x1.grid(row=0,column=0,rowspan=2)
        '''# se utliza self si quiere modificar luego el texto color etc, es decir se crea una referencia
        self.llb1 = Label(frame_x1,text="Ent") 
        self.llb1.pack(side="left")
        '''
        Label(frame_x1,text="Ent").pack(side="left") # Crea la etiqueta y la ubica no se va a poder tener acceso a Ella
        self.txt1E = Entry(frame_x1,width=4) # en los atributos Entri wl width indica la candidad de caracteres del numero
        self.txt1E.pack(side="right")
        Label(frame_funo,text="Num").grid(row=0,column=2)
        Label(frame_funo,text="Den").grid(row=1,column=2)
        self.txt1N = Entry(frame_funo,width=4) 
        self.txt1D = Entry(frame_funo,width=4) 
        self.txt1N.grid(row=0,column=1)
        self.txt1D.grid(row=1,column=1)
        
        frame_fdos = Frame(self, width=100, height=60, bg="#FFFFCD")
        frame_fdos.place(x=170,y=40)
        frame_x2 = Frame(frame_fdos,width=42,height=27, bg="#A7E8FF")
        frame_x2.grid(row=0,column=0,rowspan=2)
        Label(frame_x2,text="Ent").pack(side="left") # Crea la etiqueta y la ubica no se va a poder tener acceso a Ella
        self.txt2E = Entry(frame_x2,width=4) # en los atributos Entri wl width indica la candidad de caracteres del numero
        self.txt2E.pack(side="right")
        Label(frame_fdos,text="Num").grid(row=0,column=2)
        Label(frame_fdos,text="Den").grid(row=1,column=2)
        self.txt2N = Entry(frame_fdos,width=4) 
        self.txt2D = Entry(frame_fdos,width=4) 
        self.txt2N.grid(row=0,column=1)
        self.txt2D.grid(row=1,column=1)
        Label(self,text="Fraccion Uno").place(x=50,y=15)
        Label(self,text="Fraccion Dos").place(x=190,y=15)
        Label(self,text="Operacion").place(x=30,y=150)
        Label(self,text="Resultado").place(x=30,y=90)
        ''' vamos a cambiar el objecto entry por el objecto texto Largo
        self.txtres = Entry(self,width=15)
        self.txtres.place(x=100,y=120)
        '''
        ''' Ahora vamos a colocar un scrollbar para ello tenemos que crear un Contenedor para el Texto y el scroll
        self.txtres = Text(self,width=15,height=3)
        self.txtres.place(x=100,y=120)
        '''
        faux = Frame(self)
        faux.place(x=100,y=90) # la misma posicion que tenia anteriormente el objecto texto
        sbar = Scrollbar(faux)
        self.txtres = Text(faux,width=15,height=3, yscrollcommand=sbar.set)
        self.txtres.pack(side='left')
        sbar.config(command=self.txtres.yview)
        sbar.pack(side='right',fill='y')

        self.btncal = Button(self,text="Calcular",command=self.fcalcular)
        self.btncal.place(x=220,y=150)
        self.opciones = ["Suma","Resta","Multiplicación","División","Son Iguales?"]
        self.cbopciones = Combobox(self, width="10",values=self.opciones, state="readonly")
        self.cbopciones.place(x=100,y=150)
        self.cbopciones.current(0) # inicializa las opciones en el primer valor

        '''
        Creando un RadioButton
        como no se hace referencia al r1..r2..r3 sini a la variable var_op
        cambia el disemño
        r1 = Radiobutton(self,text=self.opciones[0], value=0, variable=self.var_op)
        r1.place(x=100,y=180)
        r2 = Radiobutton(self,text=self.opciones[1], value=1, variable=self.var_op)
        r2.place(x=100,y=200)
        r3 = Radiobutton(self,text=self.opciones[2], value=2, variable=self.var_op)
        r3.place(x=100,y=220)
        r4 = Radiobutton(self,text=self.opciones[3], value=3, variable=self.var_op)
        r4.place(x=100,y=240)
        r5 = Radiobutton(self,text=self.opciones[4], value=4, variable=self.var_op)
        r5.place(x=100,y=260)
        '''
        ''' Funciona con una lista
        Radiobutton(self,text=self.opciones[0], value=0, variable=self.var_op).place(x=100,y=180)
        Radiobutton(self,text=self.opciones[1], value=1, variable=self.var_op).place(x=100,y=200)
        Radiobutton(self,text=self.opciones[2], value=2, variable=self.var_op).place(x=100,y=220)
        Radiobutton(self,text=self.opciones[3], value=3, variable=self.var_op).place(x=100,y=240)
        Radiobutton(self,text=self.opciones[4], value=4, variable=self.var_op).place(x=100,y=260)
        ''' 
        # con un Diccionario
        self.btncal2 = Button(self,text="Calcular2",command=self.fcalcular2)
        self.btncal2.place(x=220,y=220)
        dopciones = {"Suma":0,"Resta":1,"Multiplicación":2,"División":3,"Son Iguales?":4}
        posy = 180
        for (textod,valord) in dopciones.items():
            Radiobutton(self,text=textod, value=valord, variable=self.var_op).place(x=100,y=posy)
            posy += 20




        
''' se quita y se lleva a otra file
root = Tk()
root.wm_title("Fracciones Mixtas")
app = MainFrame(root)
app.mainloop()
'''