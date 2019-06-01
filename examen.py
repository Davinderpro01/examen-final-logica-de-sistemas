#Curso: Lógica de Sistemas
#Semestre: primer semestre
#Nombre: Devin Alexander Solórzano Morales
#Carné: 0907-19-8968

#librería para interfaz gráfica
from tkinter import *

# esta es la función que ejecuta las operaciones del primer botón
def operacion1():
    if int(Var1.get()) < int(Var3.get()):
        VarResultado.set("El resultado de la multiplicación es = " + str(int(Var1.get()) * int(Var2.get()) * int(Var3.get())))    
    else:    
        if int(Var1.get()) == int(Var3.get()):
            VarResultado.set("El resultado de la suma es = " + str(int(Var1.get()) + int(Var2.get()) + int(Var3.get())))
        else:    
            if int(Var2.get()) == 0:
                if int(Var1.get()) > int(Var3.get()):
                    VarResultado.set("El resultado de la resta es = " + str(int(Var1.get()) - int(Var3.get())))
                else:
                    VarResultado.set("El resultado de la resta es = " + str(int(Var3.get()) - int(Var1.get())))

# esta es la función que ejecuta las operaciones del primer botón
def operacion2():
    Valor_1 = int(Var1.get())
    Valor_2 = int(Var2.get())
    Valor_3 = int(Var3.get())
    Valoperacion = (Valor_1*Valor_2+Valor_3)
    concatenacionfor= str(Valor_1) + str(Valor_2) + str(Valor_3)
    Devinimpresion = ""
    
    #operación del bucle for
    for x in range(Valoperacion):
        Devinimpresion = Devinimpresion + concatenacionfor
    
    VarResultado.set(Devinimpresion) 

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
mensaje1 = Label(Alexander, text = 'Primer numero: ').grid(row = 1, column = 0)
Var1 = StringVar()
ingreso1 = Entry(Alexander, textvariable= Var1).grid(row = 1, column = 1, padx = 50, pady = 20)

# input2
mensaje2 =Label(Alexander, text = 'Segundo numero: ').grid(row = 2, column = 0)
Var2 = StringVar()
ingreso2 = Entry(Alexander, textvariable= Var2).grid(row = 2, column = 1, padx = 50, pady = 10)

# input3
mensaje3 =Label(Alexander, text = 'Tercer numero: ').grid(row = 3, column = 0)
Var3 = StringVar()
ingreso4 = Entry(Alexander, textvariable= Var3).grid(row = 3, column = 1, padx = 50, pady = 20)

#para crear el primer botón de opciones
Botoncito = Button(Alexander, text = "Botón 1", command = operacion1).grid(row = 4, columnspan = 2, pady = 10)

#para crear el segundo botón de opciones
Botoncito2 = Button(Alexander, text = "Botón 2", command = operacion2).grid(row = 5, columnspan = 2, pady = 10)

#para crear la pestaña en donde va a aparecer el resultado
VarResultado = StringVar()
cuadro = Entry(Alexander, textvariable=VarResultado, justify = "center").grid(row = 6, columnspan = 2, pady = 10, sticky = W + E)

#para crear oficialmente la ventana
Devin.mainloop()