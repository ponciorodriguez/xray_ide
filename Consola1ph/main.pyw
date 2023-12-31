from mammo import *
from consola import *
from consola_sed import *
from tkinter import * 
from tkinter.ttk import * 

from tkinter import Frame
import os
cwd = os.path.dirname(__file__)











main = Tk()
main.geometry("300x200")

ancho_ventana = 200
alto_ventana = 200


x_ventana = main.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = main.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
main.geometry(posicion)


main.resizable(0,0)
frame_menu = Frame(main , bg = "yellow",  width=200)
frame_menu.pack(side="left", fill="y", expand=False)
frame_generador= Frame(main , bg = "grey", height=700)
frame_generador.pack(side="top",fill="x",expand=False)
frame_teaching= Frame(main , bg = "blue", height=300)
frame_teaching.pack(side="bottom",fill="x",expand=False)
boton_sedecal = Button(frame_menu , text = "RX Sedecal" , command = sedecal )
boton_sedecal.place(x = 20 , y = 25)
boton_philips = Button(frame_menu , text = "RX Philips" , command = philips)
boton_philips.place(x = 20 , y = 75)

boton_mammo = Button(frame_menu , text = "Salir" , command = exit )
boton_mammo.place(x = 100 , y = 150)






main.mainloop()
