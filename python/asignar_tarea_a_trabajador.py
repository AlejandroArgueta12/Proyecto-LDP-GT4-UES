# ==========================================
# ARCHIVO: asignar_tarea_a_trabajador.py
# ==========================================
import tkinter as tk
from tkinter import messagebox
from pantalla_base import PantallaBase
import controlador_datos as db

class AsignarTareaATrabajador(PantallaBase):
    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Administrador", ventana_padre, panel_retorno)

        for widget in self.menu.winfo_children():
            widget.destroy()

        tk.Button(self.menu, text="✔  Asignar a proyectos", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", justify="left", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20, command=self.abrir_asignar_proyecto).pack(fill="x", pady=20)
        tk.Button(self.menu, text="✔  Asignar a trabajadores", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", justify="left", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20).pack(fill="x", pady=20)
        tk.Button(self.menu, text="✔  Asignar horas", bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, activebackground=self.COLOR_MENU, activeforeground=self.COLOR_TEXTO, bd=0, anchor="w", cursor="hand2", font=("Arial", 16, "bold"), padx=20, pady=20, command=self.abrir_asignar_horas).pack(fill="x", pady=20)
        
        self.crear_boton_retroceder()

        self.frame_central = tk.Frame(self.contenido, bg=self.COLOR_FONDO)
        self.frame_central.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(self.frame_central, text="ID de Tarea", bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=(0, 15))
        self.entry_tarea = tk.Entry(self.frame_central, width=30, font=("Arial", 12))
        self.entry_tarea.pack(ipady=5, pady=(0, 30))

        tk.Label(self.frame_central, text="ID de Trabajador", bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=(0, 15))
        self.entry_trabajador = tk.Entry(self.frame_central, width=30, font=("Arial", 12))
        self.entry_trabajador.pack(ipady=5, pady=(0, 40))

        tk.Button(self.frame_central, text="Asignar Trabajador", bg="#2f6df6", fg="white", font=("Arial", 12, "bold"), cursor="hand2", padx=25, pady=8, relief="flat", command=self.asignar).pack()

    def asignar(self):
        id_tarea = self.entry_tarea.get().strip().upper()
        id_trabajador = self.entry_trabajador.get().strip().upper()
        if not id_tarea or not id_trabajador:
            messagebox.showwarning("Advertencia", "Complete todos los campos.")
            return
        
        exito, msj = db.asignar_tarea_trabajador(id_tarea, id_trabajador)
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.entry_tarea.delete(0, tk.END)
            self.entry_trabajador.delete(0, tk.END)
        else:
            messagebox.showerror("Error", msj)

    def abrir_asignar_proyecto(self):
        from asignar_tarea_a_proyecto import AsignarTareaAProyecto
        self.ventana.destroy()
        AsignarTareaAProyecto(self.ventana_padre, self.panel_retorno)

    def abrir_asignar_horas(self):
        from asignar_horas_trabajadas import AsignarHorasTrabajadas
        self.ventana.destroy()
        AsignarHorasTrabajadas(self.ventana_padre, self.panel_retorno)