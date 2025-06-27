from tkinter import Tk
from tkinter.ttk import Treeview
def main():
    root = Tk()
    root.wm_title("Ejemplo de Treeview")
    root.geometry("600x300")
    root["bg"]="#fb0"
    tv = Treeview(root, columns=("col1","col2"))
    tv.column("#0",width=80)
    tv.column("col1",width=80, anchor='center')
    tv.column("col2",width=80, anchor='center')
    tv.heading("#0",text="Productos", anchor='center')
    tv.heading("col1",text="Precio", anchor='center')
    tv.heading("col2",text="Cantidad", anchor='center')
    tv.insert("",'end',text="Azucar", values=(28,2))
    tv.insert("",'end',text="Refresco", values=(16,3))
    tv.insert("",'end',text="Aceite", values=(34,1))
    
    tv.place(x=100,y=20)

    root.mainloop()

if __name__ == "__main__":
    main()

