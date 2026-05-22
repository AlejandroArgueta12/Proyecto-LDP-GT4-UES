# ==========================================
# ARCHIVO: ver_informes.py
# ==========================================
import tkinter as tk
from tkinter import ttk
from pantalla_base import PantallaBase
import controlador_datos as db

class VerInformes(PantallaBase):
    def __init__(self, ventana_padre=None, panel_retorno=None):
        super().__init__("Informes", ventana_padre, panel_retorno)
        
        # Limpiar menú lateral
        for widget in self.menu.winfo_children():
            widget.destroy()
        self.crear_boton_retroceder()

        # Título principal
        tk.Label(self.contenido, text="Panel de Visualización General", bg=self.COLOR_FONDO, font=("Arial", 24, "bold")).pack(pady=30)

        # Configurar estilos del Notebook y las Tablas
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Arial", 12, "bold"), padding=[20, 10])
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 11), rowheight=30)

        # Crear el contenedor de pestañas
        self.notebook = ttk.Notebook(self.contenido)
        self.notebook.pack(fill="both", expand=True, padx=40, pady=(0, 40))

        # Crear las pestañas
        self.tab_tareas = tk.Frame(self.notebook, bg="white")
        self.tab_empleados = tk.Frame(self.notebook, bg="white")
        self.tab_proyectos = tk.Frame(self.notebook, bg="white")

        self.notebook.add(self.tab_tareas, text="  📋 Tareas y Horas  ")
        self.notebook.add(self.tab_empleados, text="  👥 Empleados  ")
        self.notebook.add(self.tab_proyectos, text="  📦 Proyectos  ")

        # Construir las tablas dentro de cada pestaña
        self.construir_tabla_tareas()
        self.construir_tabla_empleados()
        self.construir_tabla_proyectos()

    # ======================================
    # TABLA: TAREAS
    # ======================================
    def construir_tabla_tareas(self):
        columnas = ("ID Tarea", "Nombre Tarea", "Proyecto", "Trabajador Asignado", "Horas Invertidas")
        self.tabla_tareas = ttk.Treeview(self.tab_tareas, columns=columnas, show="headings", height=15)
        
        for col in columnas:
            self.tabla_tareas.heading(col, text=col)
            self.tabla_tareas.column(col, anchor="center", width=150)

        self.tabla_tareas.pack(fill="both", expand=True, padx=20, pady=20)
        
        datos = db.obtener_reporte_tareas()
        for fila in datos:
            self.tabla_tareas.insert("", tk.END, values=fila)

    # ======================================
    # TABLA: EMPLEADOS
    # ======================================
    def construir_tabla_empleados(self):
        columnas = ("ID Trabajador", "Nombre Completo", "Cargo")
        self.tabla_empleados = ttk.Treeview(self.tab_empleados, columns=columnas, show="headings", height=15)
        
        for col in columnas:
            self.tabla_empleados.heading(col, text=col)
            self.tabla_empleados.column(col, anchor="center", width=250)

        self.tabla_empleados.pack(fill="both", expand=True, padx=20, pady=20)
        
        datos = db.obtener_reporte_empleados()
        for fila in datos:
            self.tabla_empleados.insert("", tk.END, values=fila)

    # ======================================
    # TABLA: PROYECTOS
    # ======================================
    def construir_tabla_proyectos(self):
        columnas = ("ID Proyecto", "Nombre del Proyecto", "Fecha de Inicio", "Fecha de Finalización")
        self.tabla_proyectos = ttk.Treeview(self.tab_proyectos, columns=columnas, show="headings", height=15)
        
        for col in columnas:
            self.tabla_proyectos.heading(col, text=col)
            self.tabla_proyectos.column(col, anchor="center", width=200)

        self.tabla_proyectos.pack(fill="both", expand=True, padx=20, pady=20)
        
        datos = db.obtener_reporte_proyectos()
        for fila in datos:
            self.tabla_proyectos.insert("", tk.END, values=fila)