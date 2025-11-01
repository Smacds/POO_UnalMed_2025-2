import tkinter as tk
import math

class CalculosNumericos:
    
    @staticmethod
    def calcularLogaritmoNeperiano(numero: float):
        try:
            resultado = math.log(numero)
            return resultado
        except ValueError:
            return "Error: El valor para el logaritmo neperiano debe ser mayor que cero."
        finally:
            print("Cálculo del logaritmo neperiano finalizado.")

    @staticmethod
    def calcularRaizCuadrada(numero: float):
        try:
            resultado = math.sqrt(numero)
            return resultado
        except ValueError:
            return "Error: El valor para la raíz cuadrada no debe ser negativo."
        finally:
            print("Cálculo de la raíz cuadrada finalizado.")

class InterfazCalculos(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora de Métodos Estáticos y Excepciones")
        self.geometry("500x300")
        
        
        self.numero_log_var = tk.DoubleVar() 
        self.numero_raiz_var = tk.DoubleVar()
        
        self.log_resultado_var = tk.StringVar(value="Esperando cálculo Ln...")
        self.raiz_resultado_var = tk.StringVar(value="Esperando cálculo √...")
        
        self.crear_widgets()

    def crear_widgets(self):
        fuente_principal = ('Arial', 12)
        fuente_boton = ('Arial', 12, 'bold')
        
        
        tk.Label(self, text="Número para Logaritmo (Ln):", font=fuente_principal).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.numero_log_var, font=fuente_principal, width=20, bd=2, relief=tk.GROOVE).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        tk.Button(self, text="Calcular Logaritmo (Ln)", font=fuente_boton, command=self.calcular_log, bg='#e1f5fe', fg='#01579b', activebackground='#b3e5fc').grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(self, textvariable=self.log_resultado_var, wraplength=200, justify=tk.LEFT, fg="#01579b", bg='#f0f0f0', relief=tk.SUNKEN, bd=1).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        
        tk.Label(self, text="Número para Raíz Cuadrada (√):", font=fuente_principal).grid(row=2, column=0, padx=10, pady=15, sticky="w")
        tk.Entry(self, textvariable=self.numero_raiz_var, font=fuente_principal, width=20, bd=2, relief=tk.GROOVE).grid(row=2, column=1, padx=10, pady=15, sticky="ew")
        
        tk.Button(self, text="Calcular Raíz Cuadrada (√)", font=fuente_boton, command=self.calcular_raiz, bg='#e8f5e9', fg='#1b5e20', activebackground='#c8e6c9').grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(self, textvariable=self.raiz_resultado_var, wraplength=200, justify=tk.LEFT, fg="#1b5e20", bg='#f0f0f0', relief=tk.SUNKEN, bd=1).grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        

    def calcular_log(self):
        try:
            numero = self.numero_log_var.get()
            resultado = CalculosNumericos.calcularLogaritmoNeperiano(numero)
            
            if isinstance(resultado, str):
                self.log_resultado_var.set(resultado)
            else:
                self.log_resultado_var.set(f"Resultado Ln({numero}): {resultado:.4f}")
            
        except tk.TclError:
            self.log_resultado_var.set("Error: Ingrese un número flotante válido.")

    def calcular_raiz(self):
        try:
            # Obtiene el valor del campo de Raíz Cuadrada
            numero = self.numero_raiz_var.get()
            resultado = CalculosNumericos.calcularRaizCuadrada(numero)
            
            if isinstance(resultado, str):
                self.raiz_resultado_var.set(resultado)
            else:
                self.raiz_resultado_var.set(f"Resultado √({numero}): {resultado:.4f}")
            
        except tk.TclError:
            self.raiz_resultado_var.set("Error: Ingrese un número flotante válido.")
       

if __name__ == "__main__":
    app = InterfazCalculos()
    app.mainloop()
