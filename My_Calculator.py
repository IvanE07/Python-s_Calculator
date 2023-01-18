#Importamos librerias, tkinter es una librería para interfaces gráficas, mientras system simplemente para limpiar la consola
from tkinter import *
from os import system

"""

PROGRAMA BY LUIS IVAN VILLEGAS ELIGIO
INGENIERIA EN COMPUTACION

I LOVE PYTHON Y LA QUE ME GUSTA <3

"""

#Limpiamos consola
system("cls")

#Variable global que nos servirá para borrar y manipular en contenido de la caja de texto
i = 0

#Asignamos a la variable ventana tk() para crear una ventana
ventana = Tk()
#Colocamos titulo a nuestra ventana
ventana.title("Villegas_Eligio My first calculator")

#Entrada de texto en el que se irá escribiendo los digitos
box_txt = Entry(ventana, font = "Tahoma 40", bg = 'green')
box_txt.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)

#Funciones:

#Funcion para agregar valores a la calculadora
def click_Button(valor):
    global i
    box_txt.insert(i, valor)
    i += 1

#Borramos o limpiamos nuestra pantalla de calculadora
def delete_Text():
    box_txt.delete(0, END)
    i = 0

#Ejecutamos las operaciones que se escriban, nos arrojará errores si los hay
def operation():
    try:
        ecuacion = box_txt.get()
        resultado = eval(ecuacion)
        box_txt.delete(0, END)
        box_txt.insert(0, resultado)
    except Exception as error:
        box_txt.delete(0, END)
        box_txt.insert(0, "MATH ERROR")

    i = 0

#Borrar un único caracter
def delete_One():
    global i
    cadena = box_txt.get()
    cadena = str(cadena[:-1])
    box_txt.delete(0, END)
    
    try:
        box_txt.insert(0, int(cadena))
    except:
        try:
            box_txt.insert(0, float(cadena))
        except:
            box_txt.insert(cadena)

    i = len(cadena)

#Botones:
#Este primer bloque serán valores númericos, añadiremos a la ventana, el texto que aparecerá en cada boton, altura y anchura
#la acción que estos tendrán y su color de fondo y el color de la fuente
#Botones númericos:
button_1 = Button(ventana, text = "1", width = 10, height = 3, command = lambda: click_Button(1), bg = '#E0EDF4', fg = 'red')
button_2 = Button(ventana, text = "2", width = 10, height = 3, command = lambda: click_Button(2), bg = '#E0EDF4', fg = 'red')
button_3 = Button(ventana, text = "3", width = 10, height = 3, command = lambda: click_Button(3), bg = '#E0EDF4', fg = 'red')
button_4 = Button(ventana, text = "4", width = 10, height = 3, command = lambda: click_Button(4), bg = '#E0EDF4', fg = 'red')
button_5 = Button(ventana, text = "5", width = 10, height = 3, command = lambda: click_Button(5), bg = '#E0EDF4', fg = 'red')
button_6 = Button(ventana, text = "6", width = 10, height = 3, command = lambda: click_Button(6), bg = '#E0EDF4', fg = 'red')
button_7 = Button(ventana, text = "7", width = 10, height = 3, command = lambda: click_Button(7), bg = '#E0EDF4', fg = 'red')
button_8 = Button(ventana, text = "8", width = 10, height = 3, command = lambda: click_Button(8), bg = '#E0EDF4', fg = 'red')
button_9 = Button(ventana, text = "9", width = 10, height = 3, command = lambda: click_Button(9), bg = '#E0EDF4', fg = 'red')
button_0 = Button(ventana, text = "0", width = 10, height = 3, command = lambda: click_Button(0), bg = '#E0EDF4', fg = 'red')

#Caso similar, confguraciones y acciones
#Botones complementos
button_Delete = Button(ventana, text = chr(9003), width = 10, height = 3, command = lambda: delete_Text(), bg = '#F52800', fg = 'white')
button_Delete_One = Button(ventana, text = "DEL", width = 10, height = 3, command = lambda: delete_One(), bg = '#F52800', fg = 'white')
button_Parentheses1 = Button(ventana, text = "(", width = 10, height = 3, command = lambda: click_Button('('), bg = '#41FA16', fg = 'black')
button_Parentheses2 = Button(ventana, text = ")", width = 10, height = 3, command = lambda: click_Button(')'), bg = '#41FA16', fg = 'black')
button_point = Button(ventana, text = ".", width = 10, height = 3, command = lambda: click_Button('.'), bg = '#41FA16', fg = 'black')
button_equal = Button(ventana, text = "=", width = 10, height = 3, command = lambda: operation(), bg = '#41FA16', fg = 'black')

#Botones de operación:
button_Sum = Button(ventana, text = "+", width = 10, height = 3, command = lambda: click_Button('+'), bg = '#80D0EB', fg = 'black')
button_Subtraction = Button(ventana, text = "-", width = 10, height = 3, command = lambda: click_Button('-'), bg = '#80D0EB', fg = 'black')
button_Multiplication = Button(ventana, text = "*", width = 10, height = 3, command = lambda: click_Button('*'), bg = '#80D0EB', fg = 'black')
button_Division = Button(ventana, text = chr(247), width = 10, height = 3, command = lambda: click_Button('/'), bg = '#80D0EB', fg = 'black')

#Acomodar botones en pantalla:
#Fila 1, columna de 0 a 3
button_Delete.grid(row = 1, column = 0, padx = 5, pady = 5)
button_Parentheses1.grid(row = 1, column = 1, padx = 5, pady = 5)
button_Parentheses2.grid(row = 1, column = 2, padx = 5, pady = 5)
button_Division.grid(row = 1, column = 3, padx = 5, pady = 5)

#Fila 2, columna de 0 a 3
button_7.grid(row = 2, column = 0, padx = 5, pady = 5)
button_8.grid(row = 2, column = 1, padx = 5, pady = 5)
button_9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_Multiplication.grid(row = 2, column = 3, padx = 5, pady = 5)

#Fila 3, columna de 0 a 3
button_4.grid(row = 3, column = 0, padx = 5, pady = 5)
button_5.grid(row = 3, column = 1, padx = 5, pady = 5)
button_6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_Subtraction.grid(row = 3, column = 3, padx = 5, pady = 5)

#Fila 4, columna de 0 a 3
button_1.grid(row = 4, column = 0, padx = 5, pady = 5)
button_2.grid(row = 4, column = 1, padx = 5, pady = 5)
button_3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_Sum.grid(row = 4, column = 3, padx = 5, pady = 5)

#Fila 5, columna de 0 a 3
button_0.grid(row = 5, column = 0, padx = 5, pady = 5)
button_Delete_One.grid(row = 5, column = 1, padx = 5, pady = 5)
button_point.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equal.grid(row = 5, column = 3, padx = 5, pady = 5)

#Asignamos un color al fondo de nuestra ventana
ventana.config(bg = '#FEF2CC')
#Un bucle para que aparezca siempre la ventana hasta que nosostros salgamos del programa
ventana.mainloop()