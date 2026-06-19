# ==========================================
# ARCHIVO: gestionar_datos.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class GestionarDatos(PantallaBase):
    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Gestión de Datos", ventana_padre, panel_retorno)

        # LIMPIAR MENU
        for widget in self.menu.winfo_children():
            widget.destroy()
        self.crear_boton_retroceder()

        tk.Label(self.contenido, text="Gestionar y Eliminar Registros", bg=self.COLOR_FONDO, font=("Arial", 28, "bold")).pack(pady=30)

        # --- SECCIÓN DE BÚSQUEDA ---
        self.frame_busqueda = tk.Frame(self.contenido, bg=self.COLOR_FONDO)
        self.frame_busqueda.pack(pady=10)

        self.tipo_var = tk.StringVar(value="empleados")
        opciones = [("Trabajador", "empleados"), ("Proyecto", "proyectos"), ("Tarea", "tareas")]
        
        frame_radios = tk.Frame(self.frame_busqueda, bg=self.COLOR_FONDO)
        frame_radios.grid(row=0, column=0, columnspan=3, pady=10)
        for texto, valor in opciones:
            tk.Radiobutton(frame_radios, text=texto, variable=self.tipo_var, value=valor, bg=self.COLOR_FONDO, font=("Arial", 12)).pack(side="left", padx=10)

        tk.Label(self.frame_busqueda, text="Ingresar ID:", bg=self.COLOR_FONDO, font=("Arial", 14, "bold")).grid(row=1, column=0, padx=5)
        self.entry_id_buscar = tk.Entry(self.frame_busqueda, font=("Arial", 14), width=15)
        self.entry_id_buscar.grid(row=1, column=1, padx=5)

        tk.Button(self.frame_busqueda, text="🔍 Buscar", bg="#1f567d", fg="white", font=("Arial", 12, "bold"), cursor="hand2", command=self.buscar_registro).grid(row=1, column=2, padx=10)

        # --- SECCIÓN DINÁMICA DE EDICIÓN ---
        self.frame_edicion = tk.Frame(self.contenido, bg=self.COLOR_FONDO)
        self.frame_edicion.pack(pady=20, fill="x")

        self.campos_editables = {}

    def buscar_registro(self):
        for widget in self.frame_edicion.winfo_children():
            widget.destroy()
        self.campos_editables.clear()

        tipo = self.tipo_var.get()
        id_obj = self.entry_id_buscar.get().strip().upper()

        if not id_obj:
            messagebox.showwarning("Advertencia", "Ingrese un ID para buscar.")
            return

        datos = db.obtener_entidad(tipo, id_obj)
        if not datos:
            messagebox.showerror("Error", f"No se encontró el ID '{id_obj}'.")
            return

        tk.Label(self.frame_edicion, text=f"Editando Registro: {id_obj}", bg=self.COLOR_FONDO, font=("Arial", 16, "bold"), fg="#1f567d").pack(pady=15)

        frame_inputs = tk.Frame(self.frame_edicion, bg=self.COLOR_FONDO)
        frame_inputs.pack()

        fila = 0
        for clave, valor in datos.items():
            if isinstance(valor, (dict, list)) or clave == "horas_invertidas" or clave == "registro_horas_diarias":
                continue

            tk.Label(frame_inputs, text=clave.capitalize() + ":", bg=self.COLOR_FONDO, font=("Arial", 12, "bold")).grid(row=fila, column=0, sticky="e", pady=8, padx=10)
            
            entry = tk.Entry(frame_inputs, font=("Arial", 12), width=35)
            entry.insert(0, str(valor) if valor is not None else "")
            entry.grid(row=fila, column=1, pady=8, padx=10)

            self.campos_editables[clave] = entry
            fila += 1

        frame_botones = tk.Frame(self.frame_edicion, bg=self.COLOR_FONDO)
        frame_botones.pack(pady=30)

        tk.Button(frame_botones, text="💾 Guardar Cambios", bg="#2f6df6", fg="white", font=("Arial", 12, "bold"), cursor="hand2", command=lambda: self.guardar_cambios(tipo, id_obj)).pack(side="left", padx=15)
        tk.Button(frame_botones, text="🗑 Eliminar", bg="#b22222", fg="white", font=("Arial", 12, "bold"), cursor="hand2", command=lambda: self.eliminar_registro(tipo, id_obj)).pack(side="left", padx=15)

    def guardar_cambios(self, tipo, id_obj):
        nuevos_datos = {}
        for clave, entry in self.campos_editables.items():
            nuevos_datos[clave] = entry.get().strip()

        confirmar = messagebox.askyesno("Confirmar", "¿Desea guardar los cambios realizados?")
        if confirmar:
            exito, msj = db.actualizar_entidad(tipo, id_obj, nuevos_datos)
            if exito:
                messagebox.showinfo("Éxito", msj)
                for widget in self.frame_edicion.winfo_children():
                    widget.destroy()
                self.entry_id_buscar.delete(0, tk.END)
            else:
                messagebox.showerror("Error", msj)

    def eliminar_registro(self, tipo, id_obj):
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el registro '{id_obj}'?\nEsta acción es irreversible.")
        if confirmar:
            exito, msj = db.eliminar_entidad(tipo, id_obj)
            if exito:
                messagebox.showinfo("Éxito", msj)
                for widget in self.frame_edicion.winfo_children():
                    widget.destroy()
                self.entry_id_buscar.delete(0, tk.END)
            else:
                messagebox.showerror("Error", msj)