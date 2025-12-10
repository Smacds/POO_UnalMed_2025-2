import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# --- CLASES DE DATOS ---

class Huesped:
    """Clase para almacenar la información del cliente"""
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

class Habitacion:
    """Clase que representa una habitación y su estado"""
    def __init__(self, numero_hab):
        self.numero = numero_hab
        # Lógica de precio según el enunciado: 1-5 ($120k), 6-10 ($160k)
        self.precio_noche = 120000 if numero_hab <= 5 else 160000
        self.esta_ocupada = False
        self.fecha_ingreso = None
        self.datos_huesped = None  # Aquí guardaremos el objeto Huesped

# --- CLASE PRINCIPAL DE LA INTERFAZ ---

class SistemaHotel:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Sistema de Gestión Hotelera")
        self.ventana_principal.geometry("400x300")

        # 1. Inicializar las 10 habitaciones
        self.lista_habitaciones = [Habitacion(i) for i in range(1, 11)]

        # 2. Configurar el Menú Superior
        barra_menu = tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=barra_menu)

        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Gestión Hotel", menu=menu_opciones)
        
        menu_opciones.add_command(label="Consultar / Registrar Ingreso", command=self.abrir_ventana_consultar)
        menu_opciones.add_command(label="Salida de Huéspedes", command=self.abrir_ventana_salida)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.ventana_principal.quit)

        # Mensaje de bienvenida
        tk.Label(self.ventana_principal, text="Bienvenido a la Recepción", font=("Arial", 16)).pack(pady=50)
        tk.Label(self.ventana_principal, text="Seleccione una opción del menú superior", fg="gray").pack()

    # ------------------------------------------------------------------
    # OPCIÓN 1: CONSULTAR Y REGISTRAR INGRESO
    # ------------------------------------------------------------------
    def abrir_ventana_consultar(self):
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Estado de Habitaciones")
        ventana.geometry("600x400")

        # Tabla (Treeview) para mostrar estados
        columnas = ("Habitación", "Precio", "Estado")
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        tabla.heading("Habitación", text="N° Habitación")
        tabla.heading("Precio", text="Precio x Noche")
        tabla.heading("Estado", text="Disponibilidad")
        
        # Centrar columnas
        for col in columnas:
            tabla.column(col, anchor="center")

        tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Llenar la tabla con datos actuales
        for hab in self.lista_habitaciones:
            estado_texto = "OCUPADA" if hab.esta_ocupada else "Disponible"
            # Formato de moneda para que se vea bien
            tabla.insert("", "end", values=(hab.numero, f"${hab.precio_noche:,.0f}", estado_texto))

        # Sección para seleccionar habitación
        frame_seleccion = tk.Frame(ventana)
        frame_seleccion.pack(pady=10)

        tk.Label(frame_seleccion, text="Seleccione N° de Habitación para Ocupar:").pack(side="left")
        entry_num_hab = tk.Entry(frame_seleccion, width=5)
        entry_num_hab.pack(side="left", padx=5)

        def verificar_y_abrir_registro():
            try:
                num = int(entry_num_hab.get())
                # Validar rango 1-10
                if num < 1 or num > 10:
                    messagebox.showerror("Error", "La habitación no existe (1-10).")
                    return
                
                # Obtener el objeto habitación (índice es numero - 1)
                hab_seleccionada = self.lista_habitaciones[num - 1]

                if hab_seleccionada.esta_ocupada:
                    messagebox.showerror("No disponible", f"La habitación {num} ya está ocupada.")
                else:
                    self.abrir_formulario_huesped(hab_seleccionada, ventana) # Pasamos 'ventana' para cerrarla luego si queremos
            
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un número válido.")

        tk.Button(frame_seleccion, text="Iniciar Registro", command=verificar_y_abrir_registro).pack(side="left", padx=10)

    def abrir_formulario_huesped(self, habitacion, ventana_padre):
        form = tk.Toplevel(self.ventana_principal)
        form.title(f"Registro - Habitación {habitacion.numero}")
        form.geometry("300x350")

        tk.Label(form, text="Fecha de Ingreso (dd/mm/yyyy):").pack(pady=5)
        entry_fecha = tk.Entry(form)
        entry_fecha.pack()

        tk.Label(form, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(form)
        entry_nombre.pack()

        tk.Label(form, text="Apellidos:").pack(pady=5)
        entry_apellido = tk.Entry(form)
        entry_apellido.pack()

        tk.Label(form, text="Documento ID:").pack(pady=5)
        entry_cedula = tk.Entry(form)
        entry_cedula.pack()

        def guardar_datos():
            # 1. Validar campos vacíos
            if not all([entry_fecha.get(), entry_nombre.get(), entry_apellido.get(), entry_cedula.get()]):
                messagebox.showwarning("Faltan datos", "Todos los campos son obligatorios.")
                return

            # 2. Validar Fecha
            try:
                fecha_obj = datetime.strptime(entry_fecha.get(), "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Fecha Error", "Formato de fecha inválido. Use dia/mes/año (ej: 01/01/2023)")
                return

            # 3. Guardar en el objeto
            habitacion.esta_ocupada = True
            habitacion.fecha_ingreso = fecha_obj
            habitacion.datos_huesped = Huesped(entry_nombre.get(), entry_apellido.get(), entry_cedula.get())

            messagebox.showinfo("Éxito", f"Habitación {habitacion.numero} asignada correctamente.")
            form.destroy()
            ventana_padre.destroy() # Cerramos la lista también para refrescar luego

        tk.Button(form, text="Guardar Registro", command=guardar_datos, bg="#dddddd").pack(pady=20)

    # ------------------------------------------------------------------
    # OPCIÓN 2: SALIDA DE HUÉSPEDES
    # ------------------------------------------------------------------
    def abrir_ventana_salida(self):
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Check-out / Salida")
        ventana.geometry("300x150")

        tk.Label(ventana, text="Ingrese N° de Habitación a entregar:").pack(pady=10)
        entry_num = tk.Entry(ventana)
        entry_num.pack()

        def procesar_salida():
            try:
                num = int(entry_num.get())
                if num < 1 or num > 10:
                    messagebox.showerror("Error", "Número fuera de rango.")
                    return
                
                hab_seleccionada = self.lista_habitaciones[num - 1]

                if not hab_seleccionada.esta_ocupada:
                    messagebox.showerror("Error", "Esta habitación está vacía, no se puede hacer Check-out.")
                    return
                
                # Si todo está bien, abrimos la ventana de cálculo
                self.abrir_calculo_pago(hab_seleccionada, ventana)
            
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido.")

        tk.Button(ventana, text="Continuar", command=procesar_salida).pack(pady=10)

    def abrir_calculo_pago(self, habitacion, ventana_anterior):
        ventana_anterior.destroy() # Cerramos la ventanita de selección
        
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title(f"Liquidación - Habitación {habitacion.numero}")
        ventana.geometry("400x400")

        # Información del Huesped
        info = (f"Huésped: {habitacion.datos_huesped.nombre} {habitacion.datos_huesped.apellido}\n"
                f"Ingreso: {habitacion.fecha_ingreso.strftime('%d/%m/%Y')}")
        tk.Label(ventana, text=info, justify="left", fg="blue").pack(pady=10)

        # Entrada Fecha Salida
        tk.Label(ventana, text="Fecha de Salida (dd/mm/yyyy):").pack()
        entry_salida = tk.Entry(ventana)
        entry_salida.pack()

        # Etiqueta para mostrar resultados
        lbl_total = tk.Label(ventana, text="Total a pagar: $0", font=("Arial", 12, "bold"))
        lbl_total.pack(pady=20)

        # --- LÓGICA DE BOTONES CONDICIONALES ---
        
        def realizar_calculo():
            try:
                fecha_salida = datetime.strptime(entry_salida.get(), "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha incorrecto.")
                return

            if fecha_salida <= habitacion.fecha_ingreso:
                messagebox.showerror("Lógica Error", "La fecha de salida debe ser POSTERIOR a la de ingreso.")
                return

            # Calcular días
            delta = fecha_salida - habitacion.fecha_ingreso
            dias_totales = delta.days
            total_pagar = dias_totales * habitacion.precio_noche

            # Actualizar etiqueta visual
            lbl_total.config(text=f"Días: {dias_totales} | Total: ${total_pagar:,.0f}")
            
            # REQUISITO CLAVE: Habilitar el botón de salida solo AHORA
            btn_confirmar.config(state="normal", bg="#90ee90") # Se pone verde y activo

        def confirmar_salida():
            # Limpiar datos de la habitación
            habitacion.esta_ocupada = False
            habitacion.datos_huesped = None
            habitacion.fecha_ingreso = None
            
            messagebox.showinfo("Salida Exitosa", "La habitación ha quedado disponible nuevamente.")
            ventana.destroy()

        # Botón 1: Calcular (Siempre activo al inicio)
        tk.Button(ventana, text="Calcular Total", command=realizar_calculo).pack(pady=5)

        # Botón 2: Confirmar (Inicia Desactivado / DISABLED)
        btn_confirmar = tk.Button(ventana, text="Registrar Salida Definitiva", 
                                  command=confirmar_salida, state="disabled")
        btn_confirmar.pack(pady=10)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaHotel(root)
    root.mainloop()
