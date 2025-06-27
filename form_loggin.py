import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.font import BOLD
import generico as utl
from form_master import MasterPanel
import time
import servicio


class App():
    def verificar(self):
        usu = self.usuario.get()
        if (usu):
            self.password.focus()
        else:
            messagebox.showinfo(message="Debe Inidicar el Usuario", title=self.ventana.title())
            self.usuario.focus()
            return
        pas = self.password.get()
        if (pas):
            pass
        else:
            messagebox.showinfo(message="Debe Inidicar la Contraseña")
            return
        if(usu=="root" and pas=="1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="El Usuario y/o Contraseña no son Validos.", title="Mensaje")

    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Login")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
        logo = utl.leer_imagen(db_path+"Imagenes/caja.jpeg",(200,200))
        # frame logo
        frame_logo = tk.Frame(self.ventana,bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#3a7ff6")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        tk.Label( frame_logo, image=logo, bg="#3a7ff6").place(x=0,y=0,relwidth=1, relheight=1)
        # frame form
        frame_form = tk.Frame(self.ventana,bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame form Top
        frame_form_top = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID, bg="black")
        frame_form_top.pack(side="top", fill=tk.X)
        tk.Label( frame_form_top, text="Inicio de Sección",font=('Times',30), fg="#666a88", bg="#fcfcfc", pady=50).pack(expand=tk.YES, fill=tk.BOTH)
        # frame form fill
        frame_form_fill = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        tk.Label( frame_form_fill, text="Usuario",font=('Times',14), fg="#666a88", bg="#fcfcfc", anchor="w").pack(fill=tk.X, padx=20, pady=5)
        self.usuario = tk.Entry(frame_form_fill, font=('Times',14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
        self.usuario.bind("<Return>", (lambda event: self.verificar()) )
        tk.Label( frame_form_fill, text="Contraseña",font=('Times',14), fg="#666a88", bg="#fcfcfc", anchor="w").pack(fill=tk.X, padx=20, pady=5)
        self.password = tk.Entry(frame_form_fill, font=('Times',14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        self.password.bind("<Return>", (lambda event: self.verificar()) )
        Inicio = tk.Button(frame_form_fill, text="Inicio Sección", font=("Times",15,BOLD),bg="#3a7ff6", bd=0, fg="#fff", command=self.verificar)
        Inicio.pack(fill=tk.X, padx=20,pady=20)
        Inicio.bind("<Return>", (lambda event: self.verificar()) )
        self.usuario.focus()
        

        self.ventana.mainloop()

