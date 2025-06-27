
import tkinter

def wf_mensaje(amensaje):
    print(amensaje)
def wf_mensaje2():
    print("Hola Francisco")


winicio = tkinter.Tk()
winicio.geometry("400x280")
winicio.title("Nombre Aplicacion")

ltext = tkinter.Label(winicio,text="Esta es un texto")
ltext.pack()

#lbtn = tkinter.Button(winicio,text="Mensaje", command=wf_mensaje("Hola Francisco"))
lbtn = tkinter.Button(winicio,text="Mensaje", command=wf_mensaje2)
lbtn.pack()

winicio.mainloop()