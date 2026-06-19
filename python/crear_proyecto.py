# ==========================================
# ARCHIVO: crear_proyecto.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class CrearProyecto(PantallaBase):

    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Administrador", ventana_padre, panel_retorno)

        # BOTONES MENU
        self.menu.winfo_children()[1].config(command=self.abrir_crear_trabajador)
        self.menu.winfo_children()[2].config(command=self.abrir_crear_tarea)

        # TITULO
        self.titulo = tk.Label(self.contenido, text="Crear Proyecto", bg="#ececec", fg="black", font=("Arial", 28, "bold"))
        self.titulo.pack(pady=(30, 20))

        # FRAME FORMULARIO
        self.frame_form = tk.Frame(self.contenido, bg="#ececec")
        self.frame_form.pack(pady=10)

        # --- COLUMNA IZQUIERDA ---
        self.frame_izquierdo = tk.Frame(self.frame_form, bg="#ececec")
        self.frame_izquierdo.pack(side="left", padx=30)

        # ID DEL PROYECTO
        tk.Label(self.frame_izquierdo, text="ID del proyecto", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_id = tk.Entry(self.frame_izquierdo, width=25, font=("Arial", 13))
        self.entry_id.pack(ipady=5, pady=(0, 20))

        # FECHA DE INICIO
        tk.Label(self.frame_izquierdo, text="Fecha de Inicio (DD/MM/AAAA)", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_inicio = tk.Entry(self.frame_izquierdo, width=25, font=("Arial", 13))
        self.entry_inicio.pack(ipady=5, pady=(0, 20))

        # --- COLUMNA DERECHA ---
        self.frame_derecho = tk.Frame(self.frame_form, bg="#ececec")
        self.frame_derecho.pack(side="left", padx=30)

        # NOMBRE PROYECTO
        tk.Label(self.frame_derecho, text="Nombre de proyecto", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_nombre = tk.Entry(self.frame_derecho, width=25, font=("Arial", 13))
        self.entry_nombre.pack(ipady=5, pady=(0, 20))

        # FECHA DE FIN
        tk.Label(self.frame_derecho, text="Fecha de Finalización (DD/MM/AAAA)", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_fin = tk.Entry(self.frame_derecho, width=25, font=("Arial", 13))
        self.entry_fin.pack(ipady=5, pady=(0, 20))

        # BOTON GUARDAR (Ubicado directamente en la sección de contenido)
        self.btn_guardar = tk.Button(self.contenido, text="Guardar Proyecto", bg="#1f567d", fg="white", font=("Arial", 14, "bold"), cursor="hand2", padx=25, pady=10, command=self.guardar_datos)
        self.btn_guardar.pack(pady=20)

    def guardar_datos(self):
        id_proyecto = self.entry_id.get().strip().upper()
        nombre = self.entry_nombre.get().strip()
        fecha_inicio = self.entry_inicio.get().strip()
        fecha_fin = self.entry_fin.get().strip()

        if not id_proyecto or not nombre or not fecha_inicio or not fecha_fin:
            messagebox.showwarning("Advertencia", "Complete todos los campos")
            return

        exito, msj = db.registrar_proyecto(id_proyecto, nombre, fecha_inicio, fecha_fin)
        if exito:
            messagebox.showinfo("Correcto", msj)
            self.entry_id.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_inicio.delete(0, tk.END)
            self.entry_fin.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msj)

    def abrir_crear_trabajador(self):
        from crear_trabajador import CrearTrabajador
        self.ventana.destroy()
        CrearTrabajador(self.ventana_padre, self.panel_retorno)

    def abrir_crear_tarea(self):
        from crear_tarea import CrearTarea
        self.ventana.destroy()
        CrearTarea(self.ventana_padre, self.panel_retorno)