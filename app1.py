#import tkinter as tk
from tkinter import Button, Frame

#class Frame_Hola(tk.Frame):
class Frame_Hola(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        #self.btn1 = tk.Button(self)
        self.btn1 = Button(self)
        self.btn1["text"] = "Hola Mundo\nClick aqui"
        self.btn1["command"] = self.say_hi
        self.btn1.pack(side="top")
        #self.btnq = tk.Button(self,text="Quit",fg="red",command=self.master.destroy)
        self.btnq = Button(self,text="Quit",fg="red",command=self.master.destroy)
        self.btnq.pack(side="bottom")
    def say_hi(self):
        print("Hola Francisco")
    
''' Se quita para dejar la clase
root = tk.Tk()
root.geometry("400x200")
appg = Frame_Hola(master=root)
appg.mainloop()
'''




