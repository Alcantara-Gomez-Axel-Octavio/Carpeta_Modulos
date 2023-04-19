from tkinter import *
from tkinter import ttk
import tkinter as ttk
from tkinter import messagebox

class Calculadora:
    def __init__(self, principal):
        self.principal = principal
        self.principal.title("Calculadora")
        principal.config(borderwidth=0, bg="white")


        self.imagen12 = PhotoImage(file= 'Fondo.png')
        self.imagen11_reducida12 = self.imagen12.subsample(1, 1)
        self.etqImagen = ttk.Label(principal)
        self.etqImagen.grid(column=0, row=0, columnspan=6, rowspan=6)
        self.etqImagen["image"]  = self.imagen11_reducida12
        self.etqImagen.config(borderwidth=0, highlightthickness=0)

        
        self.Resultados = ttk.Entry(self.principal, width=20, font=("Arial", 30), justify="right", bg="#0c94d4", foreground="white")
        self.Resultados.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
        self.Resultados.config(borderwidth=0)
        self.Resultados.focus()


        self.crearboton("/", 1, 1)
        self.crearboton(7, 1, 2)
        self.crearboton(8, 1, 3)
        self.crearboton(9, 1, 4)
        self.crearboton("^", 1, 5)
        self.crearboton("*", 2, 1)
        self.crearboton(4, 2, 2)
        self.crearboton(5, 2, 3)
        self.crearboton(6, 2, 4)
        self.crearboton("%", 2, 5)
        self.crearboton("-", 3, 1)
        self.crearboton(1, 3, 2)
        self.crearboton(2, 3, 3)
        self.crearboton(3, 3, 4)
        self.crearboton("+", 4, 1)
        self.crearboton(".", 4, 2)
        self.crearboton(0, 4, 3)
        
        self.imagen2 = PhotoImage(file= 'Borrador.png')
        self.imagen2_reducida = self.imagen2.subsample(12, 12) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
        self.etqImagen2 = ttk.Button(principal, bg="#9484c4", command=self.borrar_caracter,activebackground="#9484c9", width=80)
        self.etqImagen2.grid(column=5, row=3, pady=10, padx=15)
        self.etqImagen2['image']=self.imagen2_reducida
        self.etqImagen2.config(borderwidth=0, highlightthickness=0)


        self.botonIgual = ttk.Button(self.principal, text="=", width=15, font=("Arial", 17), command=self.calcular, bg="#ac84bc", foreground="white",activebackground="#ac84b9", activeforeground="purple")
        self.botonIgual.grid(row=4, column=4, columnspan=2, padx=10, pady=10)
        self.botonIgual.config(borderwidth=0)

    def crearboton(self, text, fila, columna):

        if(text==7 or text==8 or text==9 or text=="/" or text=="^"):
            button = ttk.Button(self.principal, text=text, width=7, font=("Arial", 17), bg="#548ccc", foreground="white", command=lambda: self.agregar_caracter(text),activebackground="#548cc9", activeforeground="purple")
            button.grid(row=fila, column=columna, padx=5, pady=5)
            button.config(borderwidth=0)
        if(text==4 or text==5 or text==6 or text=="*" or text=="%"):
            button = ttk.Button(self.principal, text=text, width=7, font=("Arial", 17), bg="#748cc4", foreground="white", command=lambda: self.agregar_caracter(text),activebackground="#748cc9", activeforeground="purple")
            button.grid(row=fila, column=columna, padx=5, pady=5)
            button.config(borderwidth=0)
        if(text==1 or text==2 or text==3 or text=="-" ):
            button = ttk.Button(self.principal, text=text, width=7, font=("Arial", 17), bg="#9484c4", foreground="white", command=lambda: self.agregar_caracter(text),activebackground="#9484c9", activeforeground="purple")
            button.grid(row=fila, column=columna, padx=5, pady=5)
            button.config(borderwidth=0)
        if(text==0 or text=="." or text=="+"):
            button = ttk.Button(self.principal, text=text, width=7, font=("Arial", 17), bg="#ac84bc", foreground="white", command=lambda: self.agregar_caracter(text),activebackground="#ac84b9", activeforeground="purple")
            button.grid(row=fila, column=columna, padx=5, pady=5)
            button.config(borderwidth=0)
        
    def agregar_caracter(self,caracter):
        self.Resultados.insert(ttk.END, caracter)
            
    def borrar_caracter(self):
        self.Resultados.delete(len(self.Resultados.get()) - 1, END)
            
    def borrar_todo(self):
        self.Resultados.delete(0, END)

    def calcular(self):
        operacion = self.Resultados.get()

        if "+" in operacion:
            operandos = operacion.split("+")
            
            try:
                operandos = [float(op) for op in operandos]    
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
               
            resultado = suma(*operandos)

        elif "-" in operacion:
            operandos = operacion.split("-")
            try:
                  operandos = [float(op) for op in operandos]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            
            resultado = resta(*operandos)

        elif "*" in operacion:
            operandos = operacion.split("*")
            try:
                  operandos = [float(op) for op in operandos]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            resultado = multiplicacion(*operandos)

        elif "/" in operacion:
            operandos = operacion.split("/")
            try:
                  operandos = [float(op) for op in operandos]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            resultado = division(*operandos)

        elif "^" in operacion:
            operandos = operacion.split("^")
            try:
                  operandos = [float(op) for op in operandos]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            resultado = potencia(*operandos)

        elif "sqrt" in operacion:
            operandos = operacion.split("sqrt")
            try:
                  operandos = [float(op) for op in operandos if op != ""]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            resultado = raiz(*operandos)

        elif "%" in operacion:
            operandos = operacion.split("%")
            try:
                  operandos = [float(op) for op in operandos]
            except:       
                messagebox.showinfo("Error", "Este dato no es valido.")
            resultado = porcentaje(*operandos)

        # Si no se encontró ninguna operación, entonces no se realiza cálculo
        else:
            resultado = ""

        # Actualizar el contenido del Entry con el resultado
        self.Resultados.delete(0, END)
        if resultado != "":
            self.Resultados.insert(END, resultado)
        
        
        

def resta(*nums):
    res = 0
    for valor in nums:
        res-= valor
    return res 
        
def suma(*nums):
    res = 0
    for valor in nums:
        res += valor
    return res
        
def potencia(base, exponente):
    res = base ** exponente
    return res
            
def division(*nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res /= nums[i]
    return res

def multiplicacion(*nums):
    res = 1
    for valor in nums:
        res *= valor
    return res
        
def raiz(numero):
    res = numero ** 0.5
    return res

def porcentaje(cantidad, porcentaje):
    return cantidad * (porcentaje / 100)

# Crear la ventana principal y la calculadora
root = ttk.Tk()
calc = Calculadora(root)
root.mainloop()