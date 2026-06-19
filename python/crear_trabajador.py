# ==========================================
# ARCHIVO: crear_trabajador.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class CrearTrabajador(PantallaBase):

    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Administrador", ventana_padre, panel_retorno)

        # BOTONES MENU
        self.menu.winfo_children()[0].config(command=self.abrir_crear_proyecto)
        self.menu.winfo_children()[2].config(command=self.abrir_crear_tarea)

        # TITULO
        self.titulo = tk.Label(self.contenido, text="Crear Trabajador", bg="#ececec", fg="black", font=("Arial", 28, "bold"))
        self.titulo.pack(pady=(30, 20))

        # FRAME FORMULARIO
        self.frame_form = tk.Frame(self.contenido, bg="#ececec")
        self.frame_form.pack(pady=10)

        # --- COLUMNA IZQUIERDA ---
        self.frame_izquierdo = tk.Frame(self.frame_form, bg="#ececec")
        self.frame_izquierdo.pack(side="left", padx=30)

        # NOMBRES
        tk.Label(self.frame_izquierdo, text="Nombres del trabajador", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_nombres = tk.Entry(self.frame_izquierdo, width=25, font=("Arial", 13))
        self.entry_nombres.pack(ipady=5, pady=(0, 20))

        # ID TRABAJADOR
        tk.Label(self.frame_izquierdo, text="ID del trabajador", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_id = tk.Entry(self.frame_izquierdo, width=25, font=("Arial", 13))
        self.entry_id.pack(ipady=5, pady=(0, 20))

        # --- COLUMNA DERECHA ---
        self.frame_derecho = tk.Frame(self.frame_form, bg="#ececec")
        self.frame_derecho.pack(side="left", padx=30)

        # APELLIDOS
        tk.Label(self.frame_derecho, text="Apellidos del trabajador", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_apellidos = tk.Entry(self.frame_derecho, width=25, font=("Arial", 13))
        self.entry_apellidos.pack(ipady=5, pady=(0, 20))

        # CARGO DEL TRABAJADOR
        tk.Label(self.frame_derecho, text="Cargo del trabajador", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_cargo = tk.Entry(self.frame_derecho, width=25, font=("Arial", 13))
        self.entry_cargo.pack(ipady=5, pady=(0, 20))

        # BOTON GUARDAR (Ubicado directamente en la sección de contenido)
        self.btn_guardar = tk.Button(self.contenido, text="Guardar Trabajador", bg="#1f567d", fg="white", font=("Arial", 14, "bold"), cursor="hand2", padx=25, pady=10, command=self.guardar_datos)
        self.btn_guardar.pack(pady=20)

    def guardar_datos(self):
        nombres = self.entry_nombres.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        id_trabajador = self.entry_id.get().strip().upper()
        cargo = self.entry_cargo.get().strip()

        if not nombres or not apellidos or not id_trabajador or not cargo:
            messagebox.showwarning("Advertencia", "Complete todos los campos")
            return

        exito, msj = db.registrar_empleado(id_trabajador, nombres, apellidos, cargo)
        if exito:
            messagebox.showinfo("Correcto", msj)
            self.entry_nombres.delete(0, tk.END)
            self.entry_apellidos.delete(0, tk.END)
            self.entry_id.delete(0, tk.END)
            self.entry_cargo.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msj)

    def abrir_crear_proyecto(self):
        from crear_proyecto import CrearProyecto
        self.ventana.destroy()
        CrearProyecto(self.ventana_padre, self.panel_retorno)

    def abrir_crear_tarea(self):
        from crear_tarea import CrearTarea
        self.ventana.destroy()
        CrearTarea(self.ventana_padre, self.panel_retorno)