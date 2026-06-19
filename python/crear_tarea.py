# ==========================================
# ARCHIVO: crear_tarea.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class CrearTarea(PantallaBase):

    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Administrador", ventana_padre, panel_retorno)

        # BOTONES MENU
        self.menu.winfo_children()[0].config(command=self.abrir_crear_proyecto)
        self.menu.winfo_children()[1].config(command=self.abrir_crear_trabajador)

        # TITULO
        self.titulo = tk.Label(self.contenido, text="Crear Tarea", bg="#ececec", fg="black", font=("Arial", 28, "bold"))
        self.titulo.pack(pady=(30, 20))

        # FRAME FORMULARIO
        self.frame_form = tk.Frame(self.contenido, bg="#ececec")
        self.frame_form.pack(pady=10)

        # --- FILA SUPERIOR (ID y Nombre) ---
        self.frame_superior = tk.Frame(self.frame_form, bg="#ececec")
        self.frame_superior.pack(pady=(0, 20))

        # ID TAREA
        self.frame_id = tk.Frame(self.frame_superior, bg="#ececec")
        self.frame_id.pack(side="left", padx=30)
        tk.Label(self.frame_id, text="ID de la tarea", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_id = tk.Entry(self.frame_id, width=25, font=("Arial", 13))
        self.entry_id.pack(ipady=5)

        # NOMBRE TAREA
        self.frame_nombre = tk.Frame(self.frame_superior, bg="#ececec")
        self.frame_nombre.pack(side="left", padx=30)
        tk.Label(self.frame_nombre, text="Nombre de la Tarea", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.entry_nombre = tk.Entry(self.frame_nombre, width=25, font=("Arial", 13))
        self.entry_nombre.pack(ipady=5)

        # --- DESCRIPCIÓN ---
        tk.Label(self.frame_form, text="Descripción de la tarea", bg="#ececec", fg="black", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        self.text_descripcion = tk.Text(self.frame_form, width=58, height=5, font=("Arial", 12))
        self.text_descripcion.pack(pady=(0, 20))

        # --- BOTON GUARDAR ---
        self.btn_guardar = tk.Button(self.contenido, text="Guardar Tarea", bg="#1f567d", fg="white", font=("Arial", 14, "bold"), cursor="hand2", padx=25, pady=10, command=self.guardar_datos)
        self.btn_guardar.pack(pady=10)

    def guardar_datos(self):
        id_tarea = self.entry_id.get().strip().upper()
        nombre = self.entry_nombre.get().strip()
        desc = self.text_descripcion.get("1.0", tk.END).strip()

        if not id_tarea or not nombre:
            messagebox.showwarning("Advertencia", "Complete los campos obligatorios")
            return

        exito, msj = db.registrar_tarea(id_tarea, nombre, desc)
        if exito:
            messagebox.showinfo("Correcto", msj)
            self.entry_id.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.text_descripcion.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", msj)

    def abrir_crear_proyecto(self):
        from crear_proyecto import CrearProyecto
        self.ventana.destroy()
        CrearProyecto(self.ventana_padre, self.panel_retorno)

    def abrir_crear_trabajador(self):
        from crear_trabajador import CrearTrabajador
        self.ventana.destroy()
        CrearTrabajador(self.ventana_padre, self.panel_retorno)