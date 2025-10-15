import tkinter as tk
import math

class Esfera:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_volumen(self) -> float:
        return (4/3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self) -> float:
        return 4 * math.pi * (self.radio ** 2)

class Cilindro:
    def __init__(self, radio: float, altura: float):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self) -> float:
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self) -> float:
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Piramide:
    def __init__(self, base: float, altura: float, apotema: float):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self) -> float:
        area_base = self.base ** 2
        return (1/3) * area_base * self.altura

    def calcular_superficie(self) -> float:
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Geométrica POO")
        
        self.crear_widgets()

    def _obtener_float(self, entry_widget, nombre_param):
        valor_str = entry_widget.get().replace(',', '.')
        try:
            valor = float(valor_str)
            if valor <= 0:
                raise ValueError(f"{nombre_param} debe ser positivo.")
            return valor
        except ValueError:
            raise ValueError(f"Ingresa un número válido y positivo para {nombre_param}.")

    def _actualizar_esfera_resultado(self, mensaje: str, es_error=False):
        self.resultado_esfera_label.config(fg="red" if es_error else "navy")
        self.resultado_esfera_var.set(mensaje)

    def _actualizar_cilindro_resultado(self, mensaje: str, es_error=False):
        self.resultado_cilindro_label.config(fg="red" if es_error else "navy")
        self.resultado_cilindro_var.set(mensaje)

    def _actualizar_piramide_resultado(self, mensaje: str, es_error=False):
        self.resultado_piramide_label.config(fg="red" if es_error else "navy")
        self.resultado_piramide_var.set(mensaje)

    def calcular_esfera(self):
        try:
            radio = self._obtener_float(self.entry_esfera_radio, "el radio")
            
            esfera = Esfera(radio)
            volumen = esfera.calcular_volumen()
            superficie = esfera.calcular_superficie()

            mensaje = (f"Volumen: {volumen:.2f} cm³\n"
                       f"Superficie: {superficie:.2f} cm²")
            
            self._actualizar_esfera_resultado(mensaje, es_error=False)

        except ValueError as e:
            self._actualizar_esfera_resultado(str(e), es_error=True)

    def calcular_cilindro(self):
        try:
            radio = self._obtener_float(self.entry_cilindro_radio, "el radio")
            altura = self._obtener_float(self.entry_cilindro_altura, "la altura")
            
            cilindro = Cilindro(radio, altura)
            volumen = cilindro.calcular_volumen()
            superficie = cilindro.calcular_superficie()

            mensaje = (f"Volumen: {volumen:.2f} cm³\n"
                       f"Superficie: {superficie:.2f} cm²")
            
            self._actualizar_cilindro_resultado(mensaje, es_error=False)
            
        except ValueError as e:
            self._actualizar_cilindro_resultado(str(e), es_error=True)

    def calcular_piramide(self):
        try:
            base = self._obtener_float(self.entry_piramide_base, "el lado de la base")
            altura = self._obtener_float(self.entry_piramide_altura, "la altura")
            apotema = self._obtener_float(self.entry_piramide_apotema, "el apotema")
            
            piramide = Piramide(base, altura, apotema)
            volumen = piramide.calcular_volumen()
            superficie = piramide.calcular_superficie()

            mensaje = (f"Volumen: {volumen:.2f} cm³\n"
                       f"Superficie: {superficie:.2f} cm²")
            
            self._actualizar_piramide_resultado(mensaje, es_error=False)
            
        except ValueError as e:
            self._actualizar_piramide_resultado(str(e), es_error=True)

    def crear_widgets(self):
        frame_cilindro = tk.LabelFrame(self.master, text="Cilindro (Radio, Altura)", padx=10, pady=10)
        frame_cilindro.pack(padx=20, pady=5, fill="x")

        tk.Label(frame_cilindro, text="Radio (cm):").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_cilindro_radio = tk.Entry(frame_cilindro, width=15)
        self.entry_cilindro_radio.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_cilindro, text="Altura (cm):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_cilindro_altura = tk.Entry(frame_cilindro, width=15)
        self.entry_cilindro_altura.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(frame_cilindro, text="Calcular Cilindro", command=self.calcular_cilindro, bg="#78C0E0").grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado_cilindro_var = tk.StringVar(self.master, value="Volumen: ---\nSuperficie: ---")
        self.resultado_cilindro_label = tk.Label(frame_cilindro, 
                                                textvariable=self.resultado_cilindro_var, 
                                                justify=tk.LEFT, 
                                                font=('Arial', 9, 'bold'),
                                                fg="navy",
                                                height=2)
        self.resultado_cilindro_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)


        frame_esfera = tk.LabelFrame(self.master, text="Esfera (Radio)", padx=10, pady=10)
        frame_esfera.pack(padx=20, pady=5, fill="x")
        
        tk.Label(frame_esfera, text="Radio (cm):").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_esfera_radio = tk.Entry(frame_esfera, width=15)
        self.entry_esfera_radio.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(frame_esfera, text="Calcular Esfera", command=self.calcular_esfera, bg="#78C0E0").grid(row=1, column=0, columnspan=2, pady=10)

        self.resultado_esfera_var = tk.StringVar(self.master, value="Volumen: ---\nSuperficie: ---")
        self.resultado_esfera_label = tk.Label(frame_esfera, 
                                               textvariable=self.resultado_esfera_var, 
                                               justify=tk.LEFT, 
                                               font=('Arial', 9, 'bold'),
                                               fg="navy",
                                               height=2)
        self.resultado_esfera_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=5)


        frame_piramide = tk.LabelFrame(self.master, text="Pirámide (Base Cuadrada)", padx=10, pady=10)
        frame_piramide.pack(padx=20, pady=5, fill="x")
        
        tk.Label(frame_piramide, text="Lado de la Base (cm):").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_piramide_base = tk.Entry(frame_piramide, width=15)
        self.entry_piramide_base.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_piramide, text="Altura (cm):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_piramide_altura = tk.Entry(frame_piramide, width=15)
        self.entry_piramide_altura.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_piramide, text="Apotema Lateral (cm):").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_piramide_apotema = tk.Entry(frame_piramide, width=15)
        self.entry_piramide_apotema.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(frame_piramide, text="Calcular Pirámide", command=self.calcular_piramide, bg="#78C0E0").grid(row=3, column=0, columnspan=2, pady=10)

        self.resultado_piramide_var = tk.StringVar(self.master, value="Volumen: ---\nSuperficie: ---")
        self.resultado_piramide_label = tk.Label(frame_piramide, 
                                                 textvariable=self.resultado_piramide_var, 
                                                 justify=tk.LEFT, 
                                                 font=('Arial', 9, 'bold'),
                                                 fg="navy",
                                                 height=2)
        self.resultado_piramide_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=5)

class Ejercicio83:
    if __name__ == "__main__":
        root = tk.Tk()
        app = CalculadoraApp(root)
        root.mainloop()
