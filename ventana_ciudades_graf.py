from tkinter import Misc, Tk, Frame
from Ventana import Ventana

def main():
    root = Tk()
    root.wm_title("Crud Pythom MySql")
    app = Ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main()

