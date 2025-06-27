from tkinter import Button, Frame, Tk

root = Tk()
root.title("Ejemplo Frame1")
root.geometry("400x400")

frame1 = Frame(root,bg="blue")
frame1.pack(expand=True,fill='both')
frame1.config(width=400,height=50)

frame2 = Frame(root,bg="yellow")
frame2.pack(expand=True,fill='both')
frame2.config(bg="orange") # cambia el color de fondo
frame2.config(cursor="pirate") # cambia el cursor dentro del frame
frame2.config(relief="sunken") # cambia el relieve
frame2.config(bd=25) # cambia el tamaño del borde
frame2.config(width=400,height=200) # cambia el tamaño 

redbtn = Button(frame1,text="Rojo", fg="red")
brownbtn = Button(frame1,text="Brown", fg="brown")
bluenbtn = Button(frame1,text="Blue", fg="blue")

redbtn.place(relx=0.05,rely=0.05,relwidth=0.25,relheight=.90)
brownbtn.place(relx=0.35,rely=0.05,relwidth=0.25,relheight=.90)
bluenbtn.place(relx=0.65,rely=0.05,relwidth=0.25,relheight=.90)

blackbtn = Button(frame2,text="Black", fg="black")
blackbtn.pack()

root.mainloop()

