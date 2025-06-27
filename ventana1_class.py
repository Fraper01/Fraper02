from tkinter import Label, Button, Entry, Frame

class Frame_suma(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=420,height=170)
        self.master=master
        self.pack()
        self.create_widgets()

    def fnsuma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        if isinstance(n1,int): # No Funciona el Get lee str
            r = int(n1) + int(n2)
        elif isinstance(n1,float):
            r = float(n1) + float(n2)
        else:
            r = float(n1) + float(n2)
        self.txt3.delete(0,'end')
        self.txt3.insert(0,r)
    def create_widgets(self):
        self.llb1 = Label(self,text="Primer Numero:", bg="yellow", anchor="e")
        self.llb1.place(x=10,y=10,width=120,height=30)
        self.llb2 = Label(self,text="Segundo Numero:", bg="yellow", anchor="e")
        self.llb2.place(x=10,y=50,width=120,height=30)
        self.llb3 = Label(self,text="Resultado:", bg="yellow", anchor="e")
        self.llb3.place(x=10,y=120,width=120,height=30)
        self.txt1 = Entry(self, bg="pink", justify="center")
        self.txt1.place(x=140,y=10,width=120,height=30)
        self.txt2 = Entry(self, bg="pink", justify="center")
        self.txt2.place(x=140,y=50,width=120,height=30)
        self.txt3 = Entry(self, bg="pink", justify="center")
        self.txt3.place(x=140,y=120,width=120,height=30)
        self.btn1 = Button(self,text="Sumar",  anchor="center", command=self.fnsuma)
        self.btn1.place(x=270,y=50,width=80,height=30)

''' Se quita para dejar la clase sola
root = Tk()
root.wm_title("Suma de Numeros")
app = Frame_suma(root)
app.mainloop()
'''
