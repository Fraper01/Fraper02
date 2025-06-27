import tkinter 
def wf_mensaje2():
    print("Hola Francisco")
def close_ventana():
    root.destroy()
root = tkinter.Tk() 
wframe = tkinter.Frame()
wframe.config(width="800",height="240")
wframe.config(background="red")
ltext = tkinter.Label(root,text="Esta es un texto")
ltext2 = tkinter.Label(root,text="Esta es dos texto")
#ltext.pack()
#ltext2.pack()
ltext.grid(row=2,column=2)
ltext2.grid(row=0,column=0)
ltext.config(background="red")
#wframe.pack()
wframe.grid(row=1,column=1)
cb_uno = tkinter.Button(root,text="Boton Uno",padx="50",pady="05",state="active")
cb_uno.grid(row=1,column=1)
cb_uno["state"] = tkinter.DISABLED
cb_uno["state"] = tkinter.ACTIVE
cb_dos = tkinter.Button(root,text="Cerrar",padx="50",pady="05",state="active",command=close_ventana)
cb_dos.grid(row=2,column=1)
#cb_dos["activebackground"] = "blue"
cb_dos["activeforeground"] = "white"
cb_dos.config(activebackground= "blue")
cb_dos.config(state= "active")
root.mainloop()

