# ==========================================
# ARCHIVO: asignar_tarea_a_proyecto.py
# ==========================================

import tkinter as tk

from pantalla_base import PantallaBase


class AsignarTareaAProyecto(PantallaBase):

    def __init__(
        self,
        ventana_padre=None,
        panel_retorno=None
    ):

        super().__init__(
            "Administrador",
            ventana_padre,
            panel_retorno
        )

        # ======================================
        # LIMPIAR MENU
        # ======================================

        for widget in self.menu.winfo_children():

            widget.destroy()

        # ======================================
        # BOTON ASIGNAR A PROYECTOS
        # ======================================

        self.btn_proyectos = tk.Button(
            self.menu,
            text="✔  Asignar tareas a\n       proyectos",
            bg=self.COLOR_MENU,
            fg=self.COLOR_TEXTO,
            activebackground=self.COLOR_MENU,
            activeforeground=self.COLOR_TEXTO,
            bd=0,
            anchor="w",
            justify="left",
            cursor="hand2",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=20
        )

        self.btn_proyectos.pack(
            fill="x",
            pady=20
        )

        # ======================================
        # BOTON ASIGNAR A TRABAJADORES
        # ======================================

        self.btn_trabajadores = tk.Button(
            self.menu,
            text="✔  Asignar Tareas a\n       trabajadores",
            bg=self.COLOR_MENU,
            fg=self.COLOR_TEXTO,
            activebackground=self.COLOR_MENU,
            activeforeground=self.COLOR_TEXTO,
            bd=0,
            anchor="w",
            justify="left",
            cursor="hand2",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=20,
            command=self.abrir_asignar_trabajador
        )

        self.btn_trabajadores.pack(
            fill="x",
            pady=20
        )

        # ======================================
        # BOTON ASIGNAR HORAS
        # ======================================

        self.btn_horas = tk.Button(
            self.menu,
            text="✔  Asignar horas",
            bg=self.COLOR_MENU,
            fg=self.COLOR_TEXTO,
            activebackground=self.COLOR_MENU,
            activeforeground=self.COLOR_TEXTO,
            bd=0,
            anchor="w",
            cursor="hand2",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=20,
            command=self.abrir_asignar_horas
        )

        self.btn_horas.pack(
            fill="x",
            pady=20
        )

        # ======================================
        # BOTON RETROCEDER
        # ======================================

        self.crear_boton_retroceder()

        # ======================================
        # FRAME CENTRAL
        # ======================================

        self.frame_central = tk.Frame(
            self.contenido,
            bg=self.COLOR_FONDO
        )

        self.frame_central.place(
            relx=0.5,
            rely=0.45,
            anchor="center"
        )

        # ======================================
        # BUSCAR TAREA
        # ======================================

        self.label_tarea = tk.Label(
            self.frame_central,
            text="Buscar Tarea",
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO,
            font=("Arial", 18, "bold")
        )

        self.label_tarea.pack(
            pady=(0, 15)
        )

        self.frame_tarea = tk.Frame(
            self.frame_central,
            bg=self.COLOR_FONDO
        )

        self.frame_tarea.pack(
            pady=(0, 60)
        )

        self.entry_tarea = tk.Entry(
            self.frame_tarea,
            width=30,
            font=("Arial", 12)
        )

        self.entry_tarea.pack(
            side="left",
            ipady=5
        )

        self.btn_buscar_tarea = tk.Button(
            self.frame_tarea,
            text="🔍",
            font=("Arial", 14),
            cursor="hand2"
        )

        self.btn_buscar_tarea.pack(
            side="left",
            padx=5
        )

        # ======================================
        # BUSCAR PROYECTO
        # ======================================

        self.label_proyecto = tk.Label(
            self.frame_central,
            text="Buscar Proyecto",
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO,
            font=("Arial", 18, "bold")
        )

        self.label_proyecto.pack(
            pady=(0, 15)
        )

        self.frame_proyecto = tk.Frame(
            self.frame_central,
            bg=self.COLOR_FONDO
        )

        self.frame_proyecto.pack(
            pady=(0, 70)
        )

        self.entry_proyecto = tk.Entry(
            self.frame_proyecto,
            width=30,
            font=("Arial", 12)
        )

        self.entry_proyecto.pack(
            side="left",
            ipady=5
        )

        self.btn_buscar_proyecto = tk.Button(
            self.frame_proyecto,
            text="🔍",
            font=("Arial", 14),
            cursor="hand2"
        )

        self.btn_buscar_proyecto.pack(
            side="left",
            padx=5
        )

        # ======================================
        # BOTON ASIGNAR
        # ======================================

        self.btn_asignar = tk.Button(
            self.frame_central,
            text="Asignar Tarea",
            bg="#2f6df6",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            padx=25,
            pady=8,
            relief="flat"
        )

        self.btn_asignar.pack()

    # ======================================
    # ABRIR ASIGNAR TRABAJADOR
    # ======================================

    def abrir_asignar_trabajador(self):

        from asignar_tarea_a_trabajador import (
            AsignarTareaATrabajador
        )

        self.ventana.destroy()

        AsignarTareaATrabajador(
            self.ventana_padre,
            self.panel_retorno
        )

    # ======================================
    # ABRIR ASIGNAR HORAS
    # ======================================

    def abrir_asignar_horas(self):

        from asignar_horas_trabajadas import (
            AsignarHorasTrabajadas
        )

        self.ventana.destroy()

        AsignarHorasTrabajadas(
            self.ventana_padre,
            self.panel_retorno
        )