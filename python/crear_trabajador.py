# ==========================================
# ARCHIVO: crear_trabajador.py
# ==========================================

import tkinter as tk

from pantalla_base import PantallaBase


class CrearTrabajador(PantallaBase):

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
        # BOTONES MENU
        # ======================================

        # CREAR PROYECTO
        self.menu.winfo_children()[0].config(
            command=self.abrir_crear_proyecto
        )

        # CREAR TAREA
        self.menu.winfo_children()[2].config(
            command=self.abrir_crear_tarea
        )

        # ======================================
        # TITULO
        # ======================================

        self.titulo = tk.Label(
            self.contenido,
            text="Crear Trabajador",
            bg="#ececec",
            fg="black",
            font=("Arial", 28, "bold")
        )

        self.titulo.pack(
            pady=(60, 60)
        )

        # ======================================
        # FRAME PRINCIPAL
        # ======================================

        self.frame_form = tk.Frame(
            self.contenido,
            bg="#ececec"
        )

        self.frame_form.pack()

        # ======================================
        # FILA SUPERIOR
        # ======================================

        self.frame_superior = tk.Frame(
            self.frame_form,
            bg="#ececec"
        )

        self.frame_superior.pack(
            pady=(0, 40)
        )

        # ======================================
        # NOMBRES
        # ======================================

        self.frame_nombres = tk.Frame(
            self.frame_superior,
            bg="#ececec"
        )

        self.frame_nombres.pack(
            side="left",
            padx=50
        )

        self.label_nombres = tk.Label(
            self.frame_nombres,
            text="Nombres del trabajador",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_nombres.pack(
            pady=(0, 15)
        )

        self.entry_nombres = tk.Entry(
            self.frame_nombres,
            width=25,
            font=("Arial", 13)
        )

        self.entry_nombres.pack(
            ipady=6
        )

        # ======================================
        # APELLIDOS
        # ======================================

        self.frame_apellidos = tk.Frame(
            self.frame_superior,
            bg="#ececec"
        )

        self.frame_apellidos.pack(
            side="left",
            padx=50
        )

        self.label_apellidos = tk.Label(
            self.frame_apellidos,
            text="Apellidos del trabajador",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_apellidos.pack(
            pady=(0, 15)
        )

        self.entry_apellidos = tk.Entry(
            self.frame_apellidos,
            width=25,
            font=("Arial", 13)
        )

        self.entry_apellidos.pack(
            ipady=6
        )

        # ======================================
        # ID TRABAJADOR
        # ======================================

        self.frame_id = tk.Frame(
            self.frame_form,
            bg="#ececec"
        )

        self.frame_id.pack()

        self.label_id = tk.Label(
            self.frame_id,
            text="ID del trabajador",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_id.pack(
            pady=(0, 15)
        )

        self.entry_id = tk.Entry(
            self.frame_id,
            width=25,
            font=("Arial", 13)
        )

        self.entry_id.pack(
            ipady=6
        )

        # ======================================
        # BOTON GUARDAR
        # ======================================

        self.btn_guardar = tk.Button(
            self.frame_form,
            text="Guardar Trabajador",
            bg="#1f567d",
            fg="white",
            font=("Arial", 14, "bold"),
            cursor="hand2",
            padx=20,
            pady=10
        )

        self.btn_guardar.pack(
            pady=50
        )

    # ======================================
    # ABRIR CREAR PROYECTO
    # ======================================

    def abrir_crear_proyecto(self):

        from crear_proyecto import CrearProyecto

        self.ventana.destroy()

        CrearProyecto(
            self.ventana_padre,
            self.panel_retorno
        )

    # ======================================
    # ABRIR CREAR TAREA
    # ======================================

    def abrir_crear_tarea(self):

        from crear_tarea import CrearTarea

        self.ventana.destroy()

        CrearTarea(
            self.ventana_padre,
            self.panel_retorno
        )