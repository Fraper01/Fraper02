from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from servicio import Servicio
from Mensaje import *
from datetime import datetime as ldt_var

class Ventas(tk.Frame):
    db_name = "database.db"
    def __init__(self, parent):
        super().__init__(parent)
        self.numero_factura_actual = self.obtener_numero_factura_actual()
        self.widgets()
    def widgets(self):
        frame1 = tk.Frame(self, bg="green",highlightbackground="green", highlightthickness=5)
        frame1.place(x=5,y=0,relwidth=0.99, height=90)
        titulo = tk.Label(frame1,text="VENTAS",bg="white")
        self.usuario = tk.Label(frame1, text="Usuario: ", bg="yellow")
        self.fecha_actual = tk.Label(frame1, text="fecha", bg="blue")
        self.hora_actual = tk.Label(frame1, text="hora", bg="red")
        self.fecha_hora_actual(self.fecha_actual,self.hora_actual)
        self.usuario_actual(self.usuario)
        titulo.grid(row=0, column=0, padx=0, sticky="nsew" , rowspan=2)
        self.usuario.grid(row=1, column=1, padx=0, sticky="nsew", columnspan=2 )
        self.fecha_actual.grid(row=0, column=3, padx=0, sticky="nsew" )
        self.hora_actual.grid(row=1, column=3, padx=0, sticky="nsew" )
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure(1, weight=1)
        frame1.columnconfigure(2, weight=1)
        frame1.columnconfigure(3, weight=1)
        frame1.rowconfigure(0, weight=1)
        frame1.rowconfigure(1, weight=1)

        lbframe = tk.LabelFrame(self,text="Informacion de las Ventas")
        lbframe.place(x=5,y=100,relwidth=0.99,height=90)
        tk.Label(lbframe,text="Numero\nFactura:",bg="green").grid(row=0, column=0, padx=5, sticky="nsew", columnspan=2 )
        tk.Label(lbframe,text="Producto:",bg="green").grid(row=0,column=3, padx=0, sticky="nsew", columnspan=2)
        tk.Label(lbframe,text="Precio:",bg="green").grid(row=0,column=6, padx=0, sticky="nsew", columnspan=2)
        tk.Label(lbframe,text="Cantidad:",bg="green").grid(row=0, column=9, padx=0, sticky="nsew",columnspan=2)

        self.numero_factura = tk.StringVar()
        self.entry_numero_factura = tk.Entry(lbframe, textvariable=self.numero_factura, state="readonly", justify="center" )
        self.entry_numero_factura.grid(row=0,column=2, padx=10, sticky="nsew")
        self.mostrar_numero_factura()

        self.entry_nombre = ttk.Combobox(lbframe, state="readonly", justify="left" )
        self.entry_nombre.grid(row=0,column=5, padx=10, sticky="nsew", columnspan=1)
        self.entry_nombre.bind("<<ComboboxSelected>>", self.actualizar_precio)
        self.cargar_productos()

        self.var_valor = tk.DoubleVar()
        self.entry_valor = tk.Entry(lbframe, textvariable=self.var_valor, state="readonly", justify="right" )
        self.entry_valor.grid(row=0,column=8, padx=10, sticky="nsew")

        self.var_cantidad = tk.IntVar()
        self.entry_cantidad = tk.Entry(lbframe, textvariable=self.var_cantidad, state="normal", justify="right" )
        self.entry_cantidad.grid(row=0, column=10, padx=10, sticky="nsew")
        self.entry_cantidad.bind("<Return>", self.in_cantidad)

        lbframe.columnconfigure(0, weight=4)
        lbframe.columnconfigure(1, weight=1)
        lbframe.columnconfigure(2, weight=1)
        lbframe.columnconfigure(3, weight=1)
        lbframe.columnconfigure(4, weight=4)
        lbframe.columnconfigure(5, weight=1)
        lbframe.columnconfigure(6, weight=1)
        lbframe.columnconfigure(7, weight=4)
        lbframe.columnconfigure(8, weight=1)
        lbframe.columnconfigure(9, weight=4)
        lbframe.columnconfigure(10, weight=1)
        #lbframe.rowconfigure(0, weight=1)

        '''
        treeframe = tk.LabelFrame(self,text="Informacion de los Productos")
        #treeframe.place(x=150,y=220,width=800,height=200)
        treeframe.grid(row=2,column=0)
        scrol_y = tk.Scrollbar(treeframe, orient="vertical")
        scrol_y.pack(side="right", fill=Y)
        scrol_x = tk.Scrollbar(treeframe, orient="horizontal")
        scrol_x.pack(side="bottom", fill=X)
        self.treevie = ttk.Treeview(treeframe, columns=("Producto","Precio","Cantidad","SubTotal"),
                                    show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.treevie.yview)
        scrol_x.config(command=self.treevie.xview)
        self.treevie.heading("#1",text="Producto")
        self.treevie.heading("#2",text="Precio")
        self.treevie.heading("#3",text="Cantidad")
        self.treevie.heading("#4",text="SubTotal")
        self.treevie.column("Producto",anchor="center")
        self.treevie.column("Precio",anchor="center")
        self.treevie.column("Cantidad",anchor="center")
        self.treevie.column("SubTotal",anchor="center")
        self.treevie.pack(expand=TRUE, fill="both")
        lbframe2 = tk.LabelFrame(self,text="Opciones")
        #lbframe2.place(x=5,y=540,width=1090,height=90)
        lbframe2.grid(row=4,column=0)
        botom_Agregar = tk.Button(lbframe2,text="Agregar Articulo",bg="#dddddd",font="san 12 bold", command=self.registrar).place(x=50,y=10,width=240,height=50)
        botom_Pagar = tk.Button(lbframe2,text="Pagar",bg="#dddddd",font="san 12 bold", command=self.abrir_ventana_pago).place(x=400,y=10,width=240,height=50)
        botom_ver_Factura = tk.Button(lbframe2,text="Ver Factura",bg="#dddddd",font="san 12 bold", command=self.abrir_ventana_factura).place(x=750,y=10,width=240,height=50)
        frame2 = tk.Frame(self, bg="green",highlightbackground="green", highlightthickness=5)
        frame2.grid(row=3,column=0)
        self.label_suma_total = tk.Label(frame2, text="Total a Pagar: EUR 0", bg="#C6D9E3", font="sans 25 bold")
        self.label_suma_total.place(x=360,y=435)
        '''
    
    def cargar_productos(self):
        lsql = "SELECT nombre FROM inventario;"
        productos = Servicio.run_query(lsql,adb_name=self.db_name)
        self.entry_nombre["values"] = [productos[0] for productos in productos]
        if not productos:
            messagebox.showinfo("Conexion",Mensaje.ERROR_CARGAR_PRODUCTOS)

    def actualizar_precio(self, event):
        nombre_producto = self.entry_nombre.get()
        lsql = "SELECT precio FROM inventario WHERE nombre = ?;"
        lparm = (nombre_producto,)
        precio = Servicio.run_query(lsql, lparm, adb_name=self.db_name)
        if (precio):
            self.entry_valor.config(state="normal")
            self.entry_valor.delete(0,END)
            self.entry_valor.insert(0, precio[0])
            self.entry_valor.config(state="readonly")
        else:
            self.entry_valor.config(state="normal")
            self.entry_valor.delete(0,END)
            self.entry_valor.insert(0, 0)
            self.entry_valor.config(state="readonly")
            messagebox.showinfo("Conexion",Mensaje.ERROR_CARGAR_PRECIO)

    def actualizar_total(self):
        total = 0.0
        for child in self.treevie.get_children():
            subtotal = float(self.treevie.item(child,"values")[3])
            total += subtotal
        total = round(total,2)
        self.label_suma_total.config(text=f"Total a Pagar: EUR {total:}")

    def registrar(self):
        producto = self.entry_nombre.get()
        precio = self.entry_valor.get()
        cantidad = self.entry_cantidad.get()
        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad)
                if not self.verificar_stock(producto, cantidad):
                    messagebox.showerror("Error",Mensaje.ERROR_STOCK)
                    return
                precio = float(precio)
                subtotal = round(cantidad * precio,2)
                self.treevie.insert("",END,values=(producto,precio,cantidad,subtotal))
                self.entry_nombre.set("")
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0,END)
                self.entry_valor.config(state="readonly")
                self.entry_cantidad.delete(0,END)
                self.actualizar_total()
                self.entry_nombre.focus()
            except ValueError:
                messagebox.showerror("Error",Mensaje.ERROR_CANTIDAD)
        else:
            messagebox.showerror("Error",Mensaje.CAMPOS_FALTANTES)

    def verificar_stock(self, nombre_producto, cantidad):
        lsql = "SELECT stock FROM inventario WHERE nombre= ?;"
        lparam = (nombre_producto,)
        stock = Servicio.run_query(lsql, lparam, adb_name=self.db_name, atupla=1)
        if stock and int(stock[0]) >= cantidad:
            return TRUE
        return FALSE
    
    def obtener_total(self):
        total = 0.0
        for child in self.treevie.get_children():
            subtotal = float(self.treevie.item(child,"values")[3])
            total += subtotal
        return round(total,2)
    
    def abrir_ventana_pago(self):
        if not self.treevie.get_children():
            messagebox.showerror("Error",Mensaje.CAMPOS_FALTANTES)
            return
        ventana_pago = Toplevel(self)
        ventana_pago.title("Realizar Pago")
        ventana_pago.geometry("400x400")
        ventana_pago.config(bg="#C6D9E3")
        ventana_pago.resizable(False,False)
        Label(ventana_pago,bg="#C6D9E3", text=f"Total a Pagar. EUR {self.obtener_total():}",font="san 14 bold").place(x=70,y=20)
        Label(ventana_pago,bg="#C6D9E3", text="Cantidad Pagada. EUR",font="san 14 bold").place(x=100,y=90)
        entry_cantidad_pagada = Entry(ventana_pago,font="san 14 bold")
        entry_cantidad_pagada.place(x=100,y=130)
        label_cambio = Label(ventana_pago,bg="#C6D9E3", text="",font="san 14 bold")
        label_cambio.place(x=100,y=190)

        def calcular_cambio():
            try:
                cantidad_pagada = float(entry_cantidad_pagada.get())
                total = self.obtener_total()
                cambio = round(cantidad_pagada - total,2)
                if cambio < 0:
                    messagebox.showerror("Error",Mensaje.ERROR_PAGO)
                    return
                label_cambio.config(text=f"Vuelto EUR: {cambio}")
            except ValueError:
                messagebox.showerror("Error",Mensaje.ERROR_PAGO)

        tk.Button(ventana_pago,text="Calcular Vuelto", bg="white", font="san 12 bold", command=calcular_cambio).place(x=100,y=240,width=240,height=40)
        tk.Button(ventana_pago,text="Pagar", bg="white", font="san 12 bold", command=lambda: self.pagar(ventana_pago,entry_cantidad_pagada,label_cambio)).place(x=100,y=300,width=240,height=40)

    def pagar(self, ventana_pago, entry_cantidad_pagada, label_cambio):
        try:
            cantidad_pagada = float(entry_cantidad_pagada.get())
            total = self.obtener_total()
            cambio = cantidad_pagada - total
            if cambio <0:
                messagebox.showerror("Error",Mensaje.ERROR_PAGO)
                return
            try:
                for child in self.treevie.get_children():
                    item = self.treevie.item(child,"values")
                    nombre_producto = item[0]
                    cantidad_vendida = int(item[2])
                    if not self.verificar_stock(nombre_producto, cantidad_vendida):
                        messagebox.showerror("Error",f"Stock insuficiente para el Producto {nombre_producto}")
                        return
                    lsql = "INSERT INTO ventas(factura, nombre_articulo, valor_articulo, cantidad, subtotal) VALUES(?,?,?,?,?);"
                    lparm = (self.numero_factura_actual,nombre_producto, float(item[1]), cantidad_vendida, float(item[3]))
                    Servicio.run_query(lsql, lparm, adb_name=self.db_name)
                    lsql = "UPDATE inventario SET stock = stock - ? WHERE nombre = ?;"
                    lparm = (cantidad_vendida, nombre_producto)
                    Servicio.run_query(lsql, lparm, adb_name=self.db_name)
                messagebox.showinfo("Exito", "Venta registrada Exitosamente.")
                self.numero_factura_actual += 1
                self.mostrar_numero_factura()
                for child in self.treevie.get_children():
                    self.treevie.delete(child)
                ventana_pago.destroy()
            except ValueError:
                messagebox.showerror("Error","Error en Base de Datos")

        except ValueError:
            messagebox.showerror("Error","Cantidad Pagada no Valida.")
    
    def obtener_numero_factura_actual(self):
        try:
            lsql = "SELECT max(factura) FROM ventas;"
            max_factura = Servicio.run_query(lsql, adb_name=self.db_name, atupla=1)
            max_factura = max_factura[0]
            if max_factura:
                return max_factura + 1
            else:
                return 1
        except:
            return 1
    
    def mostrar_numero_factura(self):
        self.numero_factura.set(self.numero_factura_actual)

    def abrir_ventana_factura(self):
        messagebox.showwarning("Vergacion","No la hice")

    def in_cantidad(self,*args):
        try:
            producto = self.entry_nombre.get()
            precio = self.entry_valor.get()
            if producto and precio:
                valor = int(self.entry_cantidad.get())
                if valor > 0:
                    self.registrar()
                else:
                    messagebox.showerror("Error","Cantidad del Producto no Valida.")
                    self.entry_cantidad.focus()
                    return
            else:
                messagebox.showwarning("Advertencia","Debe Seleccionar un Producto.")
                self.entry_nombre.focus()
                return
        except ValueError:
            messagebox.showerror("Error","Cantidad del Producto no Valida.")
            self.entry_cantidad.focus()
            return
        
    def fecha_hora_actual(self, afecha_label, ahora_label):
        now = ldt_var.now()
        hoy = now.date()
        afecha_label.config(text= f"Fecha: {hoy.day}/{hoy.month}/{hoy.year}")
        ahora_label.config(text= f"Hora: {now.hour}:{now.minute}:{now.second}")

    def usuario_actual(self, ausuario):
        ls_usuario = "Francisco Pérez"
        ausuario.config(text= f"Usuario: {ls_usuario}")

        


            











            


        

        






