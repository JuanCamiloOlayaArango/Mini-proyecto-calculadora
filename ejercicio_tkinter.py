import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def init_window():
    window = Tk()
    window.title("Calculadora")
    window.geometry('400x300')
    ventana = ttk.Notebook(window)
    ven1 = ttk.Frame(ventana)
    ven2 = ttk.Frame(ventana)
    ventana.add(ven1, text='Operaciones Básicas')
    ventana.add(ven2, text='Ecuación Cuadrática')
    lbl1 = Label(ven1, text='')
    lbl1.grid(column=0, row=0)
    lbl2 = Label(ven2, text='')
    lbl2.grid(column=0, row=0)
    ventana.pack(expand=1, fill='both')

    label = tk.Label(ven1, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    entrada1 = tk.Entry(ven1, width=10)
    entrada2 = tk.Entry(ven1, width=10)
    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(ven1, text='Ingrese el primer dígito:', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(ven1, text='Ingrese el segundo dígito:', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(ven1, text='Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column=0, row=3)
    combo_operadores = ttk.Combobox(ven1)
    combo_operadores['values']=['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(ven1, text='Resultado:', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)

    label_raiz = tk.Label(ven1, text='Raíz: ', font=('Arial bold', 15))
    label_raiz.grid(column=0, row=8)

    def calculadora(num1, num2, operador):
      if operador == '+':
        resultado = num1+num2
      elif operador == '-':
        resultado = num1-num2
      elif operador == '*':
        resultado = num1 * num2
      elif operador == '/':
        resultado = round(num1/num2,2)
      elif operador == 'pow':
        resultado = num1**num2
      return resultado

    def click_calcular(label, num1, num2, operador):
      valor1 = float(num1)
      valor2 = float(num2)
      res = calculadora(valor1, valor2, operador)
      label.configure(text= 'Resultado: '+str(res))

    def valor(label, num):
      if num == '':
          messagebox.showerror('Error', 'Debe ingresar un valor en la casilla')
      else:
          num = float(num)
          raiz = round(num**(1/2),2)
          label.configure(text='Raíz: '+str(raiz))

    boton = tk.Button(ven1, command=lambda: click_calcular(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get()),text='Calcular', bg="purple", fg="white")
    boton.grid(column=1, row=4)
    raiz1 = tk.Radiobutton(ven1, text='Raíz del primer valor', value=1, command=lambda: valor(label_raiz, entrada1.get()))
    raiz1.grid(column=0, row=6)
    raiz2 = tk.Radiobutton(ven1, text='Raíz del segundo valor', value=2, command=lambda: valor(label_raiz, entrada2.get()))
    raiz2.grid(column=0, row=7)

    #VENTANA 2

    variable1 = tk.Entry(ven2, width=10)
    variable2 = tk.Entry(ven2, width=10)
    variable3 = tk.Entry(ven2, width=10)
    variable1.grid(column=1, row=1)
    variable2.grid(column=1, row=2)
    variable3.grid(column=1, row=3)

    label_variable1 = tk.Label(ven2, text='Coeficiente 1:', font=('Arial bold', 10))
    label_variable1.grid(column=0, row=1)
    label_variable2 = tk.Label(ven2, text='Coeficiente 2:', font=('Arial bold', 10))
    label_variable2.grid(column=0, row=2)
    label_variable3 = tk.Label(ven2, text='Coeficiente 3:', font=('Arial bold', 10))
    label_variable3.grid(column=0, row=3)

    label_cuadratica = tk.Label(ven2, text='Variables:', font=('Arial bold', 12))
    label_cuadratica.grid(column=0, row=5)

    def cuadratica(a, b, c):
        if a == '' or b == '' or c=='':
            return messagebox.showerror('Error', 'Debe ingresar un coeficiente')
        else:
            d = (b ** 2) - (4 * a * c)
            e = (d) ** (1 / 2)
            X1 = (-b + e) / (2 * a)
            X2 = (-b - e) / (2 * a)
            if d < 0:
                return 'Sin Soluciones Reales'
            elif X1 >= X2:
                return f'x1={round(X1, 2)}  y  x2={round(X2, 2)}'
            elif X2 > X1:
                return f'x1={round(X2, 2)}  y  x2={round(X1, 2)}'

    def click_cuadrado(label, c1, c2, c3):
      a = float(c1)
      b = float(c2)
      c = float(c3)
      res = cuadratica(a, b, c)
      label.configure(text= 'Variables: '+str(res))

    boton = tk.Button(ven2, command=lambda: click_cuadrado(label_cuadratica, variable1.get(), variable2.get(), variable3.get()), text='Calcular', bg="yellow", fg="black")
    boton.grid(column=1, row=4)

    window.mainloop()

def main():
  init_window()
main()