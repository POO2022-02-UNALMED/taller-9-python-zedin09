from tkinter import Tk, Button, Entry, StringVar


root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("300x260")
operacion = ""
resultado = 0
reset_pantalla = False


numeroPantalla = StringVar()
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), justify="right",
                 textvariable=numeroPantalla)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="ew")

def numeroPulsado(num):
    global operacion
    global reset_pantalla
    global num1

    if reset_pantalla != False:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)



def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(resultado)


num1 = 0
contador_resta = 0


def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1

    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta += 1
    operacion = "resta"
    reset_pantalla = True


contador_multi = 0


def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_multi += 1
    operacion = "multiplicacion"
    reset_pantalla = True


contador_divi = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_divi += 1
    operacion = "division"
    reset_pantalla = True

def elResulado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
        resultado = 0
        contador_divi = 0

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=lambda: numeroPulsado("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",
                     command=lambda: elResulado()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2",
                     borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
                   command=lambda: suma(numeroPantalla.get())).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
                     command=lambda: resta(numeroPantalla.get())).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                              cursor="hand2", command=lambda: multiplica(numeroPantalla.get())).grid(row=3, column=3,
                                                                                                     padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                        cursor="hand2", command=lambda: divide(numeroPantalla.get())).grid(row=4, column=3, padx=1,
                                                                                           pady=1)

root.mainloop()