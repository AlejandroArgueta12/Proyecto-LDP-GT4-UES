# ==========================================
# ARCHIVO: asignar_horas_trabajadas.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class AsignarHorasTrabajadas(PantallaBase):
    def __init__(self, ventana_padre=None, panel_retorno=None):
        
        titulo = "Administrador"
        if panel_retorno and panel_retorno.__class__.__name__ != "PanelAdmin":
            titulo = "Trabajador"

        super().__init__(titulo, ventana_padre, panel_retorno)

        for widget in self.menu.winfo_children():
            widget.destroy()

        if panel_retorno and panel_retorno.__class__.__name__ == "PanelAdmin":
            tk.Button(self.menu, text="✔  Asignar a proyectos", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", justify="left", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20, command=self.abrir_asignar_proyecto).pack(fill="x", pady=20)
            tk.Button(self.menu, text="✔  Asignar a trabajadores", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", justify="left", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20, command=self.abrir_asignar_trabajador).pack(fill="x", pady=20)
            tk.Button(self.menu, text="✔  Asignar horas", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20).pack(fill="x", pady=20)
        else:
            tk.Button(self.menu, text="✔  Registrar mis horas", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", font=("Arial", 16, "bold"), padx=20, pady=20, state="disabled").pack(fill="x", pady=20)
        
        self.crear_boton_retroceder()

        self.frame_central = tk.Frame(self.contenido, bg=self.COLOR_FONDO)
        self.frame_central.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(self.frame_central, text="ID de Tarea", bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=(0, 5))
        self.entry_tarea = tk.Entry(self.frame_central, width=30, font=("Arial", 12))
        self.entry_tarea.pack(ipady=5, pady=(0, 20))

        tk.Label(self.frame_central, text="Fecha (DD/MM/AAAA)", bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=(0, 5))
        self.entry_fecha = tk.Entry(self.frame_central, width=30, font=("Arial", 12))
        self.entry_fecha.pack(ipady=5, pady=(0, 20))

        tk.Label(self.frame_central, text="Horas trabajadas", bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=(0, 5))
        self.entry_horas = tk.Entry(self.frame_central, width=30, font=("Arial", 12))
        self.entry_horas.pack(ipady=5, pady=(0, 30))

        self.btn_guardar = tk.Button(self.frame_central, text="Guardar Horas", bg="#2f6df6", fg="white", font=("Arial", 12, "bold"), cursor="hand2", padx=25, pady=8, relief="flat", command=self.guardar_horas)
        self.btn_guardar.pack()

    def guardar_horas(self):
        id_tarea = self.entry_tarea.get().strip().upper()
        fecha = self.entry_fecha.get().strip()
        horas = self.entry_horas.get().strip()
        
        if not id_tarea or not fecha or not horas:
            messagebox.showwarning("Advertencia", "Complete todos los campos.")
            return
        
        exito, msj = db.registrar_horas_tarea(id_tarea, horas, fecha)
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.entry_tarea.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)
            self.entry_horas.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msj)

    def abrir_asignar_proyecto(self):
        from asignar_tarea_a_proyecto import AsignarTareaAProyecto
        self.ventana.destroy()
        AsignarTareaAProyecto(self.ventana_padre, self.panel_retorno)

    def abrir_asignar_trabajador(self):
        from asignar_tarea_a_trabajador import AsignarTareaATrabajador
        self.ventana.destroy()
        AsignarTareaATrabajador(self.ventana_padre, self.panel_retorno)