from tkinter import Tk, Frame, Menu, messagebox, Toplevel
from container import Container
from ttkthemes import ThemedStyle
from Mensaje import *
from ventas import Ventas

class Manager(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Caja")
        self.resizable(True, True)
        self.config(bg="lightblue")
        li_width = self.winfo_width()
        li_height = self.winfo_height()
        lp_width = self.winfo_screenwidth()
        lp_height = self.winfo_screenheight()
        print(li_width)
        print(li_height)
        print(lp_width)
        print(lp_height)
        self.geometry("800x400+400+220")
        li_width = self.winfo_width()
        li_height = self.winfo_height()
        lp_width = self.winfo_screenwidth()
        lp_height = self.winfo_screenheight()
        print(li_width)
        print(li_height)
        print(lp_width)
        print(lp_height)
        self.container = Frame(self, bg="lightblue")
        self.container.pack(fill="both",expand=True)
        self.frames = {
            Container : None
        }
        self.load_frames()
        self.show_frame(Container)
        self.set_theme()
        self.widgets()
    
    def ventas(self):
        self.show_fames(Ventas)

    def widgets(self):
        barra_menu=Menu(self)
        menuArchivo = Menu(barra_menu,tearoff=0)
        menuArchivo.add_command(label="Ventas",command=self.ventas)
        menuArchivo.add_command(label="Inventario")
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=self.salirAplicacion)
        barra_menu.add_cascade(label="Inicio", menu=menuArchivo)
        ayudamenu=Menu(barra_menu,tearoff=0)
        ayudamenu.add_command(label="Acerca" )
        barra_menu.add_cascade(label="Ayuda",menu=ayudamenu)
        self.config(menu=barra_menu)

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame
            
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
  
    def show_fames(self, container):
        top_level = Toplevel(self)
        frame = container(top_level)
        frame.config(bg="lightblue")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(True,True)
        top_level.grab_set()

    def set_theme(self):
        style = ThemedStyle(self)
        style.set_theme("breeze")

    def salirAplicacion(self):
	    valor=messagebox.askquestion(title="Salir",message=Mensaje.SALIR)
	    self.destroy() if valor=="yes" else None
    
def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()



