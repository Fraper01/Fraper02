from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime as ldt_var
import generico as utl
import os

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack(fill='both', expand=1)
        padre.columnconfigure(0, weight=1)
        padre.rowconfigure(0, weight=1)
        self.widgets()
    def show_fames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="lightblue")
        frame.pack(fill="both", expand=TRUE)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(TRUE,TRUE)
    def ventas(self):
        #self.show_fames(Ventas)
        pass
    def inventario(self):
        #self.show_fames(Inventario)
        pass
    def widgets(self):
        self.filler = tk.Label(self, text="", bg="red")
        self.usuario = tk.Label(self, text="Usuario: ", bg="yellow")
        ls_fileLogo = utl.get_gdic_general("ImgPath")+utl.get_gdic_general("Logo")
        if os.path.exists(ls_fileLogo):
            self.logo_imagen = Image.open(ls_fileLogo)
            self.logo_imagen = self.logo_imagen.resize((380,380))
            self.logo_imagen = ImageTk.PhotoImage(self.logo_imagen)
            self.logo_label = tk.Label(self, image=self.logo_imagen, bg = "yellow")
        else:
            self.logo_label = tk.Label(self, text="Logo", bg = "yellow")
        copyright_label = tk.Label(self,text="Elaborado por FP-2024", bg="red")
        self.fecha_actual = tk.Label(self, text="fecha", bg="yellow")
        self.hora_actual = tk.Label(self, text="hora", bg="yellow")
        self.fecha_hora_actual(self.fecha_actual,self.hora_actual)
        self.usuario_actual(self.usuario)
        self.filler.grid(row=0, column=0, padx=0, columnspan=3, sticky="nsew")
        self.logo_label.grid(row=1, column=1, padx=0, rowspan=3, sticky="nsew")
        copyright_label.grid(row=3, column=1, padx=0, sticky="nsew")
        self.fecha_actual.grid(row=2, column=2, padx=0, sticky="nsew")
        self.hora_actual.grid(row=3, column=2, padx=0, sticky="nsew" )
        self.usuario.grid(row=2, column=0, padx=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
    
    def fecha_hora_actual(self, afecha_label, ahora_label):
        now = ldt_var.now()
        hoy = now.date()
        afecha_label.config(text= f"Fecha: {hoy.day}/{hoy.month}/{hoy.year}")
        ahora_label.config(text= f"Hora: {now.hour}:{now.minute}:{now.second}")

    def usuario_actual(self, ausuario):
        ls_usuario = utl.get_gdic_general("UserName")
        ausuario.config(text= f"Usuario: {ls_usuario}")
