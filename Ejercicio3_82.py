import tkinter as tk
import numpy as np

class CalculadoraEstadisticaApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Estadística Simple")

        
        self.entradas = []
        self.resultado_promedio = tk.StringVar(value="Promedio: -")
        self.resultado_desviacion = tk.StringVar(value="Desviación Estándar: -")
        self.resultado_mayor = tk.StringVar(value="Nota Mayor: -")
        self.resultado_menor = tk.StringVar(value="Nota Menor: -")


        self.crear_widgets(master)

    def crear_widgets(self, master):
   
        for i in range(5):
            tk.Label(master, text=f"Número {i+1}:").grid(row=i, column=0, padx=5, pady=5, sticky='w')
            entrada = tk.Entry(master, width=15)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas.append(entrada)

       
        tk.Button(master, text="Calcular", command=self.calcular_operaciones).grid(row=5, column=0, padx=5, pady=10, sticky='ew')
        tk.Button(master, text="Limpiar", command=self.limpiar_informacion).grid(row=5, column=1, padx=5, pady=10, sticky='ew')

     
        tk.Label(master, text="-"*30).grid(row=6, column=0, columnspan=2, pady=5)
        
        tk.Label(master, textvariable=self.resultado_promedio, fg="blue", justify=tk.LEFT).grid(row=7, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        tk.Label(master, textvariable=self.resultado_desviacion, fg="blue", justify=tk.LEFT).grid(row=8, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        tk.Label(master, textvariable=self.resultado_mayor, fg="green", justify=tk.LEFT).grid(row=9, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        tk.Label(master, textvariable=self.resultado_menor, fg="red", justify=tk.LEFT).grid(row=10, column=0, columnspan=2, padx=5, pady=2, sticky='w')

    def obtener_numeros(self):
       
        numeros = []
        for entrada in self.entradas:
            try:
              
                num = float(entrada.get().strip())
                numeros.append(num)
            except ValueError:
               
                return []
        return numeros

    def calcular_operaciones(self):
       
        numeros = self.obtener_numeros()
        
        if not numeros or len(numeros) < 5:
   
            error_msg = "Error: 5 números válidos requeridos"
            self.resultado_promedio.set(f"Promedio: {error_msg}")
            self.resultado_desviacion.set(f"Desviación Estándar: {error_msg}")
            self.resultado_mayor.set(f"Nota Mayor: {error_msg}")
            self.resultado_menor.set(f"Nota Menor: {error_msg}")
            return

       
        promedio = np.mean(numeros)

     
        desviacion = np.std(numeros, ddof=1) if len(numeros) > 1 else 0.0


        nota_mayor = np.max(numeros)

        
        nota_menor = np.min(numeros)

        
        self.resultado_promedio.set(f"Promedio: {promedio:.2f}")
        self.resultado_desviacion.set(f"Desviación Estándar: {desviacion:.2f}")
        self.resultado_mayor.set(f"Nota Mayor: {nota_mayor:.2f}")
        self.resultado_menor.set(f"Nota Menor: {nota_menor:.2f}")

    def limpiar_informacion(self):
   
        
        for entrada in self.entradas:
            entrada.delete(0, tk.END)
            
        
        self.resultado_promedio.set("Promedio: -")
        self.resultado_desviacion.set("Desviación Estándar: -")
        self.resultado_mayor.set("Nota Mayor: -")
        self.resultado_menor.set("Nota Menor: -")


class Ejercicio82:
    if __name__ == "__main__":
        root = tk.Tk()
        app = CalculadoraEstadisticaApp(root)
        root.mainloop()