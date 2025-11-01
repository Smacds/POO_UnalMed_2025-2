import tkinter as tk

class Division:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def dividir(self):
        try:
            print("Ingresando al primer try")
            cociente= self.numerador / self.denominador
            print("Imprimiendo objeto")
            return cociente
        
        except ZeroDivisionError:
            mensaje_error="Error: División por cero no permitida."
            return mensaje_error
        finally:
            mensaje_final= "Operación de división finalizada."
            print(mensaje_final)
    
    def prueba_excepciones():
        try:
            print("Ingresando al segundo try")
            objeto=None
            objeto.algo()
            print("Imprimiendo objeto")
        except ZeroDivisionError:
            print("División por cero")
        except Exception:
            print("Ocurrió una excepción")
            return "Ocurrió una excepción genérica"
            
        finally:
            print("Ingresando al segundo finally")

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de División")
        self.geometry("700x600")
        self.numerador_var=tk.DoubleVar()
        self.denominador_var=tk.DoubleVar()
        self.entrada2= tk.DoubleVar()

        self.resultado_var=tk.StringVar(value="Esperando división...")
        self.resultador2_var=tk.StringVar(value="Esperando prueba de excepciones...")

        self.crear_widgets()
        
    def crear_widgets(self):
        tk.Label(self, text="Numerador:", font=("Times New Roman", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.numerador_var, font=("Times New Roman", 14)).grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        tk.Label(self, text="Denominador:", font=("Times New Roman", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.denominador_var, font=("Times New Roman", 14)).grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        tk.Button(self, text="Dividir", font=("Times New Roman", 14), command=self.ejecutar_division).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Label(self, textvariable=self.resultado_var, font=("Times New Roman", 14)).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        tk.Label(self, text="Se ingresará un None, pero igual ingresa algo", font=("Times New Roman", 14)).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.entrada2, font=("Times New Roman", 14)).grid(row=4, column=2, padx=10, pady=10, sticky="e")
        tk.Button(self, text="Probar Excepciones", font=("Times New Roman", 14), command=self.ejecutar_prueba_excepcion).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Label(self, textvariable=self.resultador2_var, font=("Times New Roman", 14)).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def ejecutar_division(self):
        numerador = self.numerador_var.get()
        denominador = self.denominador_var.get()
        division = Division(numerador, denominador)
        resultado = division.dividir()
        self.resultado_var.set(resultado)
        
    def ejecutar_prueba_excepcion(self):
        objeto=Division.prueba_excepciones()
        self.resultador2_var.set(objeto)

class Lanzar_interfaz:
    if __name__=="__main__":
        Interfaz().mainloop()