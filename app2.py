#import tkinter as tk
from tkinter import Tk

from ventana1_class import Frame_suma
from app1 import Frame_Hola

    
#root = tk.Tk()
root = Tk()
root.geometry("400x200")
appg = Frame_Hola(master=root)
appg = Frame_suma(master=root)
appg.mainloop()




