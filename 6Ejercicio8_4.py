import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# --- CLASE DE DATOS (Lógica pura) ---
class Empleado:
    def __init__(self, nombre, apellido, cargo, genero, sueldo_diario, dias_laborados, ingresos_extra, deduccion_salud, deduccion_pension):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.genero = genero
        self.sueldo_diario = sueldo_diario
        self.dias_laborados = dias_laborados
        self.ingresos_extra = ingresos_extra
        self.deduccion_salud = deduccion_salud
        self.deduccion_pension = deduccion_pension

    def calcular_neto(self):
        """Aplica la fórmula: (días * diario) + extras - salud - pensión"""
        basico = self.dias_laborados * self.sueldo_diario
        total = basico + self.ingresos_extra - self.deduccion_salud - self.deduccion_pension
        return total

# --- CLASE DE INTERFAZ (GUI) ---
class SistemaNomina:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Gestión de Nómina Corporativa")
        self.ventana_principal.geometry("400x300")
        
        # Lista para almacenar objetos Empleado
        self.lista_empleados = []

        # Configuración del Menú
        barra_superior = tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=barra_superior)

        menu_acciones = tk.Menu(barra_superior, tearoff=0)
        barra_superior.add_cascade(label="Gestión de Empleados", menu=menu_acciones)
        
        menu_acciones.add_command(label="Registrar Nuevo Empleado", command=self.abrir_formulario_registro)
        menu_acciones.add_separator()
        menu_acciones.add_command(label="Calcular y Ver Nómina", command=self.mostrar_tabla_nomina)
        menu_acciones.add_command(label="Exportar a TXT", command=self.exportar_archivo)
        menu_acciones.add_separator()
        menu_acciones.add_command(label="Salir", command=self.ventana_principal.quit)

        # Mensaje de bienvenida en la pantalla principal
        tk.Label(self.ventana_principal, text="Bienvenido al Sistema de Nómina", font=("Arial", 14)).pack(pady=50)
        tk.Label(self.ventana_principal, text="Use el menú superior para comenzar.", font=("Arial", 10)).pack()

    def abrir_formulario_registro(self):
        """Ventana para agregar datos, usando los widgets solicitados"""
        ventana_reg = tk.Toplevel(self.ventana_principal)
        ventana_reg.title("Registro de Empleado")
        ventana_reg.geometry("400x450")

        # Usamos Grid para alinear mejor etiquetas y campos
        marco = tk.Frame(ventana_reg, padx=20, pady=20)
        marco.pack(fill="both", expand=True)

        # Variables de control para widgets especiales
        var_cargo = tk.StringVar()
        var_genero = tk.StringVar(value="Masculino")

        # --- FILA 0: Nombre ---
        tk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(marco, width=25)
        entry_nombre.grid(row=0, column=1, pady=5)

        # --- FILA 1: Apellido ---
        tk.Label(marco, text="Apellidos:").grid(row=1, column=0, sticky="w", pady=5)
        entry_apellido = tk.Entry(marco, width=25)
        entry_apellido.grid(row=1, column=1, pady=5)

        # --- FILA 2: Cargo (JList -> Combobox) ---
        tk.Label(marco, text="Cargo:").grid(row=2, column=0, sticky="w", pady=5)
        combo_cargo = ttk.Combobox(marco, textvariable=var_cargo, state="readonly", width=22)
        combo_cargo['values'] = ("Directivo", "Estratégico", "Operativo")
        combo_cargo.current(2) # Seleccionar Operativo por defecto
        combo_cargo.grid(row=2, column=1, pady=5)

        # --- FILA 3: Género (JCheckBox/Radio) ---
        tk.Label(marco, text="Género:").grid(row=3, column=0, sticky="w", pady=5)
        frame_radio = tk.Frame(marco)
        frame_radio.grid(row=3, column=1, sticky="w")
        tk.Radiobutton(frame_radio, text="M", variable=var_genero, value="Masculino").pack(side="left")
        tk.Radiobutton(frame_radio, text="F", variable=var_genero, value="Femenino").pack(side="left")

        # --- FILA 4: Salario Día ---
        tk.Label(marco, text="Salario por día ($):").grid(row=4, column=0, sticky="w", pady=5)
        entry_sueldo = tk.Entry(marco, width=25)
        entry_sueldo.grid(row=4, column=1, pady=5)

        # --- FILA 5: Días Trabajados (JSpinner -> Spinbox) ---
        tk.Label(marco, text="Días trabajados:").grid(row=5, column=0, sticky="w", pady=5)
        spin_dias = tk.Spinbox(marco, from_=1, to=31, width=23)
        spin_dias.grid(row=5, column=1, pady=5)

        # --- FILA 6: Otros Ingresos ---
        tk.Label(marco, text="Otros ingresos ($):").grid(row=6, column=0, sticky="w", pady=5)
        entry_otros = tk.Entry(marco, width=25)
        entry_otros.grid(row=6, column=1, pady=5)

        # --- FILA 7: Salud ---
        tk.Label(marco, text="Pago salud ($):").grid(row=7, column=0, sticky="w", pady=5)
        entry_salud = tk.Entry(marco, width=25)
        entry_salud.grid(row=7, column=1, pady=5)

        # --- FILA 8: Pensión ---
        tk.Label(marco, text="Aporte pensión ($):").grid(row=8, column=0, sticky="w", pady=5)
        entry_pension = tk.Entry(marco, width=25)
        entry_pension.grid(row=8, column=1, pady=5)

        # --- FUNCIÓN INTERNA PARA GUARDAR ---
        def guardar_datos():
            try:
                # Validar campos vacíos básicos
                if not entry_nombre.get() or not entry_apellido.get():
                    messagebox.showwarning("Faltan datos", "El nombre y apellido son obligatorios.")
                    return

                nuevo_emp = Empleado(
                    nombre=entry_nombre.get(),
                    apellido=entry_apellido.get(),
                    cargo=combo_cargo.get(),
                    genero=var_genero.get(),
                    sueldo_diario=float(entry_sueldo.get()),
                    dias_laborados=int(spin_dias.get()),
                    ingresos_extra=float(entry_otros.get()),
                    deduccion_salud=float(entry_salud.get()),
                    deduccion_pension=float(entry_pension.get())
                )
                
                self.lista_empleados.append(nuevo_emp)
                messagebox.showinfo("Éxito", f"Empleado {nuevo_emp.nombre} agregado correctamente.")
                ventana_reg.destroy() # Cerrar ventana al terminar

            except ValueError:
                messagebox.showerror("Error de Tipo", "Por favor verifique que los campos numéricos contengan solo números.")

        # Botón Guardar
        tk.Button(marco, text="Guardar Registro", command=guardar_datos, bg="#dddddd").grid(row=9, column=0, columnspan=2, pady=20)

    def mostrar_tabla_nomina(self):
        """Muestra la tabla con los cálculos y el total"""
        ventana_tabla = tk.Toplevel(self.ventana_principal)
        ventana_tabla.title("Nómina Calculada")
        ventana_tabla.geometry("600x400")

        # Definir columnas
        cols = ("Nombre", "Apellido", "Cargo", "Salario Neto")
        tree = ttk.Treeview(ventana_tabla, columns=cols, show="headings")
        
        # Configurar cabeceras
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Llenar datos
        total_empresa = 0.0
        for emp in self.lista_empleados:
            sueldo_neto = emp.calcular_neto()
            total_empresa += sueldo_neto
            tree.insert("", "end", values=(emp.nombre, emp.apellido, emp.cargo, f"${sueldo_neto:,.2f}"))

        # Etiqueta de total
        lbl_total = tk.Label(ventana_tabla, text=f"TOTAL NÓMINA EMPRESA: ${total_empresa:,.2f}", 
                             font=("Arial", 12, "bold"), fg="darkblue")
        lbl_total.pack(pady=15)

    def exportar_archivo(self):
        """Genera el archivo TXT"""
        if not self.lista_empleados:
            messagebox.showwarning("Vacío", "No hay empleados registrados para exportar.")
            return

        directorio = filedialog.askdirectory(title="Seleccione carpeta para guardar")
        
        if directorio:
            ruta_completa = f"{directorio}/Nómina.txt"
            try:
                with open(ruta_completa, "w", encoding="utf-8") as f:
                    f.write("REPORTE DE NÓMINA\n")
                    f.write("="*40 + "\n\n")
                    
                    total_gral = 0
                    for emp in self.lista_empleados:
                        neto = emp.calcular_neto()
                        total_gral += neto
                        f.write(f"Empleado: {emp.nombre} {emp.apellido}\n")
                        f.write(f"Cargo: {emp.cargo} | Género: {emp.genero}\n")
                        f.write(f"A pagar: ${neto:,.2f}\n")
                        f.write("-" * 20 + "\n")
                    
                    f.write(f"\nTOTAL GENERAL EMPRESA: ${total_gral:,.2f}")
                
                messagebox.showinfo("Guardado", f"Archivo generado exitosamente en:\n{ruta_completa}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaNomina(root)
    root.mainloop()
