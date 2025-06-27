from tkinter import Tk
from tkinter.ttk import Treeview
def main():
    root = Tk()
    root.wm_title("Ejemplo de Treeview")
    root.geometry("400x300")
    root["bg"]="#fb0"
    tv = Treeview(root)
    item1 = tv.insert("",'end',text="Dias",open=1) # Abra Extendido el item
    tv.insert(item1,'end',text="Lunes")
    tv.insert(item1,'end',text="Martes")
    tv.insert(item1,'end',text="Miercoles")
    tv.insert(item1,'end',text="Jueves")
    tv.insert(item1,'end',text="Viernes")
    tv.insert(item1,'end',text="Sabado")
    tv.insert(item1,'end',text="Domingo")
    item2 = tv.insert("",'end',text="Colores",open=0)
    tv.insert(item2,'end',text="Azul")
    tv.insert(item2,'end',text="Amarillo")
    tv.insert(item2,'end',text="Rojo")
    tv.insert(item2,'end',text="Verde")
    
    tv.place(x=100,y=20)

    print(tv.get_children()) # Indica una lista con los Index de los Items sin parametro para la raiz
    for item in tv.get_children():
        print(tv.item(item))  # Muestra las propiedades de los Item
        for item1 in tv.get_children(item):
            print(tv.item(item1))  # Muestra las propiedades de los Item hijos
    
    

    root.mainloop()

if __name__ == "__main__":
    main()

