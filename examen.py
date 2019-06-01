#Curso: Lógica de Sistemas
#Semestre: primer semestre
#Nombre: Devin Alexander Solórzano Morales
#Carné: 0907-19-8968
#librería para interfaz gráfica
from tkinter import *

# esta es la función que ejecuta las operaciones del primer botón
def operacion1():
    if int(Vartexto1.get()) < int(Vartexto3.get()):
        VarResultado.set("El resultado de la multiplicación es = " + str(int(Vartexto1.get()) * int(Vartexto2.get()) * int(Vartexto3.get()))    
    else:    
        if int(Vartexto1.get()) == int(Vartexto3.get()):
            VarResultado.set("El resultado de la suma es = " + str(int(Vartexto1.get()) + int(Vartexto2.get()) + int(Vartexto3.get()))
        else:    
            if int(Vartexto2.get()) == 0:
                if int(Vartexto1.get()) > int(Vartexto3.get()):
                    VarResultado.set("El resultado de la resta es = " + str(int(Vartexto1.get()) - int(Vartexto3.get()))
                else:
                    VarResultado.set("El resultado de la resta es = " + str(int(Vartexto3.get()) - int(Vartexto1.get()))

#para crear la ventana
Devin = Tk()

#para darle título a la ventana
Devin.title("Devin Solórzano")

#para dale tamaño a la ventana
Devin.geometry("400x320")

#Darle diseño al frame
Alexander = LabelFrame(Devin, text = "operaciones")
Alexander.pack()

#input1
texto1 = Label(Alexander, text = 'Primer numero: ').grid(row = 1, column = 0)
Vartexto1 = StringVar()
cuadro1 = Entry(Alexander, textvariable= Vartexto1).grid(row = 1, column = 1, padx = 50, pady = 20)

# input2
texto2 =Label(Alexander, text = 'Segundo numero: ').grid(row = 2, column = 0)
Vartexto2 = StringVar()
cuadro2 = Entry(Alexander, textvariable= Vartexto2).grid(row = 2, column = 1, padx = 50, pady = 10)

# input3
texto3 =Label(Alexander, text = 'Tercer numero: ').grid(row = 3, column = 0)
Vartexto3 = StringVar()
cuadro3 = Entry(Alexander, textvariable= Vartexto3).grid(row = 3, column = 1, padx = 50, pady = 20)

#para crear el primer botón de multiplicación
Boton = Button(Alexander, text = "Botón 1", command = operacion1).grid(row = 4, columnspan = 2, pady = 10)

#para crear el botón
Boton = Button(Alexander, text = "Botón 2").grid(row = 5, columnspan = 2, pady = 10)

#para crear la pestaña en donde va a aparecer el resultado
VarResultado = StringVar()
Cuadro4 = Entry(Alexander, textvariable=VarResultado, justify = "center").grid(row = 6, columnspan = 2, pady = 10, sticky = W + E)

#para crear oficialmente la ventana
Devin.mainloop()