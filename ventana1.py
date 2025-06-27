from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Ejemplo 01")  
vent.geometry("400x200")
jLiteral= ['left', 'center', 'right'] 

def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    if isinstance(n1,int): # No Funciona el Get lee str
        r = int(n1) + int(n2)
    elif isinstance(n1,float):
        r = float(n1) + float(n2)
    else:
        r = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r)

''' Posiones Fijas en Pixels
# Etiquetas
llb1 = Label(vent,text="Primer Numero:", bg="yellow", anchor="e")
llb1.place(x=10,y=10,width=120,height=30)
llb2 = Label(vent,text="Segundo Numero:", bg="yellow", anchor="e")
llb2.place(x=10,y=50,width=120,height=30)
llb3 = Label(vent,text="Resultado:", bg="yellow", anchor="e")
llb3.place(x=10,y=120,width=120,height=30)

# Etiqueta de Entrada Valores
txt1 = Entry(vent, bg="pink", justify="center")
txt1.place(x=140,y=10,width=120,height=30)
txt2 = Entry(vent, bg="pink", justify="center")
txt2.place(x=140,y=50,width=120,height=30)
txt3 = Entry(vent, bg="pink", justify="center")
txt3.place(x=140,y=120,width=120,height=30)

# Boton
btn1 = Button(vent,text="Sumar",  anchor="center", command=fnsuma)
btn1.place(x=270,y=50,width=80,height=30)
'''

''' Posiones Fijas en Relativas
# Etiquetas
llb1 = Label(vent,text="Primer Numero:", bg="yellow", anchor="e")
llb1.place(relx=0.03,rely=0.04,relwidth=0.27,relheight=0.1)
llb2 = Label(vent,text="Segundo Numero:", bg="yellow", anchor="e")
llb2.place(relx=0.03,rely=0.17,relwidth=0.27,relheight=0.1)
llb3 = Label(vent,text="Resultado:", bg="yellow", anchor="e")
llb3.place(relx=0.03,rely=0.35,relwidth=0.27,relheight=0.1)

# Etiqueta de Entrada Valores
txt1 = Entry(vent, bg="pink", justify="center")
txt1.place(relx=0.32,rely=0.04,relwidth=0.22,relheight=0.1)
txt2 = Entry(vent, bg="pink", justify="center")
txt2.place(relx=0.32,rely=0.17,relwidth=0.22,relheight=0.1)
txt3 = Entry(vent, bg="cyan", justify="center")
txt3.place(relx=0.32,rely=0.35,relwidth=0.22,relheight=0.1)

# Boton
btn1 = Button(vent,text="Sumar",  anchor="center", command=fnsuma)
btn1.place(relx=0.60,rely=0.17,relwidth=0.20,relheight=0.1)
'''

''' Posiones Pack
# Etiquetas, label y Botones Declaracion
llb1 = Label(vent,text="Primer Numero:", bg="yellow", anchor="e")
llb2 = Label(vent,text="Segundo Numero:", bg="yellow", anchor="e")
llb3 = Label(vent,text="Resultado:", bg="yellow", anchor="e")
txt1 = Entry(vent, bg="pink", justify="center")
txt2 = Entry(vent, bg="pink", justify="center")
txt3 = Entry(vent, bg="cyan", justify="center")
btn1 = Button(vent,text="Sumar",  anchor="center", command=fnsuma)

# Etiqueta, label y Botones Posicionamiento
llb1.pack(pady=6)
txt1.pack(pady=6)
llb2.pack(pady=6)
txt2.pack(pady=6)
btn1.pack(pady=6)
llb3.pack(pady=6)
txt3.pack(pady=6)
'''

''' Posiones Grid
'''
# Etiquetas, label y Botones Declaracion
llb1 = Label(vent,text="Primer Numero:", bg="yellow", anchor="e")
llb2 = Label(vent,text="Segundo Numero:", bg="yellow", anchor="e")
llb3 = Label(vent,text="Resultado:", bg="yellow", anchor="e")
txt1 = Entry(vent, bg="pink", justify="center")
txt2 = Entry(vent, bg="pink", justify="center")
txt3 = Entry(vent, bg="cyan", justify="center")
btn1 = Button(vent,text="Sumar",  anchor="center", command=fnsuma)

# Etiqueta, label y Botones Posicionamiento
llb1.grid(row=1,column=0, padx=6, pady=6, sticky="e", ipady=6)
txt1.grid(row=1,column=1, padx=6, pady=6)
llb2.grid(row=2,column=0, padx=6, pady=6, sticky="e", ipady=6)
txt2.grid(row=2,column=1, padx=6, pady=6)
btn1.grid(row=2,column=2, padx=6, pady=6, ipadx=4, ipady=10)
llb3.grid(row=3,column=0, padx=6, pady=6, sticky="e", ipady=6)
txt3.grid(row=3,column=1, padx=6, pady=6)


vent.mainloop()