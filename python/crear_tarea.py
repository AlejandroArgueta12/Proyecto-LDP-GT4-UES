# ==========================================
# ARCHIVO: crear_tarea.py
# ==========================================

import tkinter as tk

from pantalla_base import PantallaBase


class CrearTarea(PantallaBase):

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

        # CREAR TRABAJADOR
        self.menu.winfo_children()[1].config(
            command=self.abrir_crear_trabajador
        )

        # ======================================
        # TITULO
        # ======================================

        self.titulo = tk.Label(
            self.contenido,
            text="Crear Tarea",
            bg="#ececec",
            fg="black",
            font=("Arial", 28, "bold")
        )

        self.titulo.pack(
            pady=(60, 50)
        )

        # ======================================
        # FRAME FORMULARIO
        # ======================================

        self.frame_form = tk.Frame(
            self.contenido,
            bg="#ececec"
        )

        self.frame_form.pack()

        # ======================================
        # ID TAREA
        # ======================================

        self.label_id = tk.Label(
            self.frame_form,
            text="ID de la tarea",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_id.pack(
            pady=(0, 15)
        )

        self.entry_id = tk.Entry(
            self.frame_form,
            width=30,
            font=("Arial", 13)
        )

        self.entry_id.pack(
            ipady=6,
            pady=(0, 40)
        )

        # ======================================
        # NOMBRE TAREA
        # ======================================

        self.label_nombre = tk.Label(
            self.frame_form,
            text="Nombre de la Tarea",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_nombre.pack(
            pady=(0, 15)
        )

        self.entry_nombre = tk.Entry(
            self.frame_form,
            width=30,
            font=("Arial", 13)
        )

        self.entry_nombre.pack(
            ipady=6,
            pady=(0, 40)
        )

        # ======================================
        # DESCRIPCION
        # ======================================

        self.label_descripcion = tk.Label(
            self.frame_form,
            text="Descripción de la tarea",
            bg="#ececec",
            fg="black",
            font=("Arial", 16, "bold")
        )

        self.label_descripcion.pack(
            pady=(0, 15)
        )

        self.text_descripcion = tk.Text(
            self.frame_form,
            width=35,
            height=6,
            font=("Arial", 12)
        )

        self.text_descripcion.pack()

        # ======================================
        # BOTON GUARDAR
        # ======================================

        self.btn_guardar = tk.Button(
            self.frame_form,
            text="Guardar Tarea",
            bg="#1f567d",
            fg="white",
            font=("Arial", 14, "bold"),
            cursor="hand2",
            padx=20,
            pady=10
        )

        self.btn_guardar.pack(
            pady=40
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
    # ABRIR CREAR TRABAJADOR
    # ======================================

    def abrir_crear_trabajador(self):

        from crear_trabajador import CrearTrabajador

        self.ventana.destroy()

        CrearTrabajador(
            self.ventana_padre,
            self.panel_retorno
        )