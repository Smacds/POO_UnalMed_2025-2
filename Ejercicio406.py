import tkinter as tk

class Vendedor:
    def __init__(self, nombre, apellido, edad):
        if edad < 0 or edad > 120:
            raise ValueError("Error: La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("Error: El vendedor debe ser mayor de 18 años.")
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def imprimir_datos(self):
        datos = f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}"
        return datos
    
        

class InterfazVendedor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Verificador de Edad del Vendedor")
        self.geometry("500x400")
        self.nombre_var=tk.StringVar()
        self.apellido_var=tk.StringVar()
        self.edad_var=tk.IntVar()
        self.resultado_var=tk.StringVar(value="Esperando verificación...")

        self.crear_widgets()
        
    def crear_widgets(self):
        tk.Label(self, text= "Nombre:", font=("Times New Roman", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.nombre_var, font=("Times New Roman", 14)).grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(self, text ="Apellido:", font=("Times New Roman", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.apellido_var, font=("Times New Roman", 14)).grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(self, text ="Edad:", font=("Times New Roman", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self, textvariable=self.edad_var, font=("Times New Roman", 14)).grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(self, text="Verificar Edad", font=("Times New Roman",14), command=self.ejecutar_verificacion).grid(row=3, column=0, padx=10, pady=10, sticky="ew" )
        tk.Label(self, textvariable=self.resultado_var, font=("Times New Roman", 14)).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def ejecutar_verificacion(self):

        nombre= self.nombre_var.get()
        apellido= self.apellido_var.get()
        edad= self.edad_var.get()
        try:
            vendedor= Vendedor(nombre, apellido, edad)
            self.resultado_var.set(vendedor.imprimir_datos())

        except ValueError as e:
            self.resultado_var.set(str(e))
        
class Lanzar_interfaz:
    if __name__=="__main__":
        InterfazVendedor().mainloop()