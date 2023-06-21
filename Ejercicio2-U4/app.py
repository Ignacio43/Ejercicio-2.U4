from tkinter import ttk, font
import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Ventana
        self.geometry("350x300")
        self.title("Calculo de IVA")
        
        #Posicionamiento
        
        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
         
        #Variables
        
        self.precioBase = tk.StringVar()
        self.iva = tk.DoubleVar()
        self.total = tk.DoubleVar()
        self.valor = tk.DoubleVar()
        self.ivaCalculado= tk.DoubleVar()
        
        #Labels
        tk.Label(self,text="Precio sin IVA").grid(row=1,column=0,**opts)
        tk.Label(self,text="IVA").grid(row=5,column=0,**opts)
        tk.Label(self,text="Precio con IVA").grid(row=6,column=0,**opts)
        
        #Entry
        self.precioBaseEntry = tk.Entry(textvariable=self.precioBase)
        self.precioBaseEntry.grid(row=1,column=2,**opts)
        
        #Botones
        tk.Radiobutton(self,text="IVA  21%",value=0,variable=self.iva,command=self.cambio).grid(row=2,column=0,**opts)
        tk.Radiobutton(self,text="IVA  10.5%",value=1,variable=self.iva,command=self.cambio).grid(row=3,column=0,**opts)
        tk.Button(self,text="Calcular",command=self.calcula,bg="green").grid(row=7,column=1)
        tk.Button(self,text="Salir",command=self.salir,bg="red").grid(row=7,column=2)
        
        self.mainloop()
    
    def salir(self):
        self.destroy()
    
    def cambio(self):
        if self.iva.get() == 0:
            self.valor.set(21/100)
        else:
            self.valor.set(10.5/100)
            
    def calcula(self):
        self.total.set(float(float(self.precioBase.get())+(float(self.precioBase.get()) * self.valor.get())))
        self.ivaCalculado.set(float(float(self.precioBase.get()) * self.valor.get()))
        self.muestraIva()
        self.muestraConIVA()
    
    def muestraIva(self):
        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        rounded_iva = round(self.ivaCalculado.get(), 2)
        tk.Label(self,text=rounded_iva).grid(row=5,column=1,**opts)
    
    
    def muestraConIVA(self):
        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        rounded_total = round(self.total.get(), 2)
        tk.Label(self,text=rounded_total).grid(row=6,column=1,**opts)


if __name__ == '__main__':
    aplicacion = Aplicacion()

    