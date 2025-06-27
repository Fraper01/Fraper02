import tkinter as tk
from tkinter.font import BOLD
import generico as utl

class MasterPanel:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Master")
        w , h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" %(w,h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0,height=0)
        db_path = "/Users/image/OneDrive/Documentos/PytonCurso/"
        logo = utl.leer_imagen(db_path+"Imagenes/caja.jpeg",(200,200))
        label = tk.Label(self.ventana, image=logo, bg="#3a7ff6")
        label.place(x=0,y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()




