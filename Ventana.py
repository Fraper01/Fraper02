from tkinter import Misc, Tk, Frame, Button, Label, Entry, messagebox, Scrollbar
from tkinter import ttk
from typing import Any, Literal
from clase_ciudades import Ciudades

class Ventana(Frame):
    paises = Ciudades()
    def __init__(self, master=None) -> None:
        super().__init__(master,  height=260, width=680)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarCajas("disable")
        self.habilitarbtnacc("disable")
        self.cId = -1
    def llenaDatos(self):
        datos = self.paises.consulta_ciudades()
        for fila in datos:
            self.grid.insert("","end",text=fila[0],values=(fila[1],fila[2],fila[3],fila[4]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])
    def limpiargrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    def habilitarCajas(self, estado):
        self.txtiso3.configure(state=estado)
        self.txtname.configure(state=estado)
        self.txtcapital.configure(state=estado)
        self.txtcurrency.configure(state=estado)
    def habilitarbtnope(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        self.btnModificar.configure(state=estado)
    def habilitarbtnacc(self, estado):
        self.btnCancelar.configure(state=estado)
        self.btnGuardar.configure(state=estado)
    def limpiarCajas(self):
        self.txtiso3.delete(0,"end")
        self.txtname.delete(0,"end")
        self.txtcapital.delete(0,"end")
        self.txtcurrency.delete(0,"end")
    def fNuevo(self):
        self.limpiarCajas()
        self.habilitarCajas("normal")
        self.habilitarbtnope("disable")
        self.habilitarbtnacc("normal")
        self.txtiso3.focus()
    def fModificar(self):
        selec = self.grid.focus()
        if selec=='':
            messagebox.showinfo(title="Modificar", message="Debe Seleccionar un Registro")
        else:
            row = self.grid.item(selec) # Devuelve todo 
            lid = self.grid.item(selec,"text") # Devuelve Clave #0
            valores = self.grid.item(selec,"values") # Devuelve los valores
            self.cId = lid
            self.habilitarCajas("normal")
            self.limpiarCajas()
            self.txtiso3.insert(0,valores[0])
            self.txtname.insert(0,valores[1])
            self.txtcapital.insert(0,valores[2])
            self.txtcurrency.insert(0,valores[3])
            self.habilitarbtnope("disable")
            self.habilitarbtnacc("normal")
            self.txtiso3.focus()
    def fEliminar(self):
        selec = self.grid.focus()
        if selec=='':
            messagebox.showinfo(title="Eliminar", message="Debe Seleccionar un Registro")
        else:
            row = self.grid.item(selec) # Devuelve todo 
            lid = self.grid.item(selec,"text") # Devuelve Clave #0
            valores = self.grid.item(selec,"values") # Devuelve los valores
            self.habilitarCajas("normal")
            self.limpiarCajas()
            self.txtiso3.insert(0,valores[0])
            self.txtname.insert(0,valores[1])
            self.txtcapital.insert(0,valores[2])
            self.txtcurrency.insert(0,valores[3])
            lsdata = str(lid) + ", " + valores[0] + ", " + valores[1]
            li_ret = messagebox.askquestion("Eliminar","Deseas Eliminar el Registro Seleccionado?\n\t"+lsdata)
            if li_ret == messagebox.YES:
                li_ret = self.paises.elimina_ciudades(lid)
                if li_ret == 1:
                    self.limpiargrid()
                    self.llenaDatos()
                    messagebox.showinfo("Eliminar","Registro Eliminado Satisfactoriamente")
                else:
                    messagebox.showinfo("Eliminar","Fallo la Eliminacion")
        self.limpiarCajas()
        self.habilitarCajas("disable")
    def fGuardar(self):
        lISO3 = self.txtiso3.get()
        lCountryName = self.txtname.get()
        lCapital = self.txtcapital.get()
        lCurrencyCode = self.txtcurrency.get()
        if self.cId == -1:
            li_ret = self.paises.inserta_ciudadesAt(lISO3,lCountryName,lCapital,lCurrencyCode)
        else:
            li_ret = self.paises.modifica_ciudades(self.cId,lISO3,lCountryName,lCapital,lCurrencyCode)
            self.cId = -1
        if li_ret == 1:
            messagebox.showinfo(title=self.winfo_parent(), message="Operación Exitosa")
        else:
            messagebox.showinfo(title=self.winfo_parent(), message="Operación Fallida ")
        self.limpiarCajas()
        self.limpiargrid()
        self.llenaDatos()
        self.habilitarCajas("disable")
        self.habilitarbtnacc("disable")
        self.habilitarbtnope("normal")
    def fCancelar(self):
        li_ret = messagebox.askquestion("Cancelar","Esta seguro que desea Cancelar la operacion")
        if li_ret == messagebox.YES:
            self.limpiarCajas()
            self.habilitarCajas("disable")
            self.habilitarbtnacc("disable")
            self.habilitarbtnope("normal")
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=260)
        self.btnNuevo = Button(frame1,text="Nuevo",command=self.fNuevo,bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=50,width=80,height=30)
        self.btnModificar = Button(frame1,text="Modificar",command=self.fModificar,bg="blue",fg="white")
        self.btnModificar.place(x=5,y=90,width=80,height=30)
        self.btnEliminar = Button(frame1,text="Eliminar",command=self.fEliminar,bg="blue",fg="white")
        self.btnEliminar.place(x=5,y=130,width=80,height=30)
        frame2 = Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=260)
        lbl1 = Label(frame2,text="ISO3: ",bg="#d3dde3")
        lbl1.place(x=3,y=5)
        self.txtiso3 = Entry(frame2)
        self.txtiso3.place(x=3,y=25,width=50,height=20)
        lbl2 = Label(frame2,text="Country Name: ",bg="#d3dde3")
        lbl2.place(x=3,y=55)
        self.txtname = Entry(frame2)
        self.txtname.place(x=3,y=75,width=100,height=20)
        lbl3 = Label(frame2,text="Capital: ",bg="#d3dde3")
        lbl3.place(x=3,y=105)
        self.txtcapital = Entry(frame2)
        self.txtcapital.place(x=3,y=125,width=100,height=20)
        lbl4 = Label(frame2,text="Currency Code: ",bg="#d3dde3")
        lbl4.place(x=3,y=155)
        self.txtcurrency = Entry(frame2)
        self.txtcurrency.place(x=3,y=175,width=100,height=20)
        self.btnGuardar = Button(frame2,text="Guardar",command=self.fGuardar,bg="green",fg="white")
        self.btnGuardar.place(x=10,y=210,width=60,height=30)
        self.btnCancelar = Button(frame2,text="Cancelar",command=self.fCancelar,bg="red",fg="white")
        self.btnCancelar.place(x=80,y=210,width=60,height=30)
        frame3 = Frame(self,bg="yellow")
        frame3.place(x=247,y=0,width=420,height=259)
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60,anchor="center")
        self.grid.column("col2",width=100,anchor="center")
        self.grid.column("col3",width=90,anchor="center")
        self.grid.column("col4",width=100,anchor="center")
        self.grid.heading("#0",text="Id", anchor="center")
        self.grid.heading("col1",text="ISO3",anchor="center")
        self.grid.heading("col2",text="Country Name",anchor="center")
        self.grid.heading("col3",text="Capital",anchor="center")
        self.grid.heading("col4",text="Currency Code",anchor="center")
        self.grid.pack(side="left",fill="y")
        scbar = Scrollbar(frame3,orient="vertical")
        scbar.pack(side="right",fill="y")
        self.grid.config(yscrollcommand=scbar.set)
        scbar.config(command=self.grid.yview)
        self.grid["selectmode"] = "browse"



