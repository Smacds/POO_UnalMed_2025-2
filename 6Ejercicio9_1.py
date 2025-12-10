import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Librería externa necesaria

# --- 1. CLASE DE DATOS ---
class Contacto:
    """Clase simple para representar la información de una persona"""
    def __init__(self, nombres, apellidos, fecha_nacimiento, direccion, telefono, email):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def obtener_info_formateada(self):
        """Devuelve un string ordenado para mostrar en la lista"""
        return (f"{self.nombres} {self.apellidos} | "
                f"Nac: {self.fecha_nacimiento} | "
                f"Dir: {self.direccion} | "
                f"Tel: {self.telefono} | "
                f"Email: {self.email}")

# --- 2. CLASE DE LA INTERFAZ GRÁFICA ---
class AgendaApp:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Agenda Personal")
        self.ventana.geometry("650x550")

        # Título principal
        tk.Label(self.ventana, text="Registro de Contacto", font=("Arial", 14, "bold")).pack(pady=15)

        # --- FRAME DEL FORMULARIO ---
        marco_datos = tk.Frame(self.ventana, bd=2, relief="groove", padx=20, pady=20)
        marco_datos.pack(pady=10)

        # Variables de entrada
        self.var_nombres = tk.StringVar()
        self.var_apellidos = tk.StringVar()
        self.var_direccion = tk.StringVar()
        self.var_telefono = tk.StringVar()
        self.var_email = tk.StringVar()

        # Fila 0: Nombres
        tk.Label(marco_datos, text="Nombres:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nombres = tk.Entry(marco_datos, textvariable=self.var_nombres, width=40)
        self.entry_nombres.grid(row=0, column=1, padx=10)

        # Fila 1: Apellidos
        tk.Label(marco_datos, text="Apellidos:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_apellidos = tk.Entry(marco_datos, textvariable=self.var_apellidos, width=40)
        self.entry_apellidos.grid(row=1, column=1, padx=10)

        # Fila 2: Fecha de Nacimiento (DateEntry)
        tk.Label(marco_datos, text="Fecha de Nacimiento:").grid(row=2, column=0, sticky="w", pady=5)
        self.date_picker = DateEntry(marco_datos, width=37, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.date_picker.grid(row=2, column=1, padx=10)

        # Fila 3: Dirección
        tk.Label(marco_datos, text="Dirección:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_direccion = tk.Entry(marco_datos, textvariable=self.var_direccion, width=40)
        self.entry_direccion.grid(row=3, column=1, padx=10)

        # Fila 4: Teléfono
        tk.Label(marco_datos, text="Teléfono:").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_telefono = tk.Entry(marco_datos, textvariable=self.var_telefono, width=40)
        self.entry_telefono.grid(row=4, column=1, padx=10)

        # Fila 5: Correo
        tk.Label(marco_datos, text="Correo Electrónico:").grid(row=5, column=0, sticky="w", pady=5)
        self.entry_email = tk.Entry(marco_datos, textvariable=self.var_email, width=40)
        self.entry_email.grid(row=5, column=1, padx=10)

        # --- BOTÓN DE ACCIÓN ---
        btn_agregar = tk.Button(self.ventana, text="Agregar a la Agenda", 
                                command=self.agregar_contacto, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        btn_agregar.pack(pady=15, ipadx=20)

        # --- LISTA DE CONTACTOS (ListView) ---
        tk.Label(self.ventana, text="Lista de Contactos Guardados:", font=("Arial", 10, "bold")).pack(anchor="w", padx=30)
        
        marco_lista = tk.Frame(self.ventana)
        marco_lista.pack(fill="both", expand=True, padx=30, pady=10)

        scrollbar = tk.Scrollbar(marco_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_visual = tk.Listbox(marco_lista, height=8, yscrollcommand=scrollbar.set)
        self.lista_visual.pack(side=tk.LEFT, fill="both", expand=True)
        
        scrollbar.config(command=self.lista_visual.yview)

    def agregar_contacto(self):
        # 1. Obtener datos
        nom = self.var_nombres.get()
        ape = self.var_apellidos.get()
        fec = self.date_picker.get()
        dir_ = self.var_direccion.get()
        tel = self.var_telefono.get()
        mail = self.var_email.get()

        # 2. Validar campos obligatorios
        if not nom or not ape:
            messagebox.showwarning("Faltan Datos", "Por favor ingrese al menos Nombres y Apellidos.")
            return

        # 3. Crear Objeto Contacto
        nuevo_contacto = Contacto(nom, ape, fec, dir_, tel, mail)

        # 4. Insertar en la lista visual
        self.lista_visual.insert(tk.END, nuevo_contacto.obtener_info_formateada())

        # 5. Limpiar formulario
        self.limpiar_campos()
        messagebox.showinfo("Éxito", "Contacto agregado correctamente.")

    def limpiar_campos(self):
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        # Opcional: Resetear fecha a hoy, si se desea
        # self.date_picker.set_date(datetime.now())

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
