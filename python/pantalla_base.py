# ==========================================
# ARCHIVO: pantalla_base.py
# ==========================================

import tkinter as tk

from confirmacion_logout import ConfirmacionLogout


class PantallaBase:

    def __init__(
        self,
        titulo,
        ventana_padre=None,
        panel_retorno=None
    ):

        # ======================================
        # VENTANA PADRE
        # ======================================

        self.ventana_padre = ventana_padre

        # PANEL AL QUE REGRESA
        self.panel_retorno = panel_retorno

        # ======================================
        # VENTANA
        # ======================================

        self.ventana = tk.Toplevel()

        self.ventana.title(titulo)

        self.ventana.state("zoomed")

        self.ventana.minsize(1200, 700)

        self.ventana.configure(
            bg="white"
        )

        # ======================================
        # COLORES
        # ======================================

        self.COLOR_BARRA = "#1f567d"
        self.COLOR_MENU = "#3e4d57"
        self.COLOR_TEXTO = "#ffb84d"
        self.COLOR_FONDO = "#ececec"

        # ======================================
        # EVENTO X
        # ======================================

        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar_aplicacion
        )

        # ======================================
        # BARRA SUPERIOR
        # ======================================

        self.barra = tk.Frame(
            self.ventana,
            bg=self.COLOR_BARRA,
            height=80
        )

        self.barra.pack(
            side="top",
            fill="x"
        )

        # ======================================
        # TITULO
        # ======================================

        self.label_titulo = tk.Label(
            self.barra,
            text="👤 " + titulo,
            bg=self.COLOR_BARRA,
            fg=self.COLOR_TEXTO,
            font=("Arial", 20, "bold")
        )

        self.label_titulo.place(
            relx=0.03,
            rely=0.5,
            anchor="w"
        )

        # ======================================
        # BOTON CERRAR SESION
        # ======================================

        self.btn_logout = tk.Button(
            self.barra,
            text="Cerrar Sesión",
            bg=self.COLOR_BARRA,
            fg=self.COLOR_TEXTO,
            activebackground=self.COLOR_BARRA,
            activeforeground=self.COLOR_TEXTO,
            relief="solid",
            bd=2,
            cursor="hand2",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=5,
            command=self.cerrar_sesion
        )

        self.btn_logout.place(
            relx=0.97,
            rely=0.5,
            anchor="e"
        )

        # ======================================
        # CONTENEDOR PRINCIPAL
        # ======================================

        self.principal = tk.Frame(
            self.ventana,
            bg=self.COLOR_FONDO
        )

        self.principal.pack(
            fill="both",
            expand=True
        )

        # ======================================
        # MENU LATERAL
        # ======================================

        self.menu = tk.Frame(
            self.principal,
            bg=self.COLOR_MENU,
            width=300
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(False)

        # ======================================
        # CONTENIDO
        # ======================================

        self.contenido = tk.Frame(
            self.principal,
            bg=self.COLOR_FONDO
        )

        self.contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ======================================
        # BOTONES MENU
        # ======================================

        self.crear_boton_menu(
            "📦  Crear Proyecto"
        )

        self.crear_boton_menu(
            "👤  Ingresar trabajador"
        )

        self.crear_boton_menu(
            "🧮  Crear Tarea"
        )

        self.crear_boton_retroceder()

    # ======================================
    # CREAR BOTON MENU
    # ======================================

    def crear_boton_menu(self, texto):

        boton = tk.Button(
            self.menu,
            text=texto,
            bg=self.COLOR_MENU,
            fg=self.COLOR_TEXTO,
            activebackground=self.COLOR_MENU,
            activeforeground=self.COLOR_TEXTO,
            bd=0,
            anchor="w",
            cursor="hand2",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=20
        )

        boton.pack(
            fill="x",
            pady=15
        )

        return boton

    # ======================================
    # BOTON RETROCEDER
    # ======================================

    def crear_boton_retroceder(self):

        self.btn_retroceder = tk.Button(
            self.menu,
            text="⬅  Retroceder",
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
            command=self.retroceder
        )

        self.btn_retroceder.pack(
            fill="x",
            pady=15
        )

    # ======================================
    # RETROCEDER
    # ======================================

    def retroceder(self):

        self.ventana.destroy()

        if self.panel_retorno:

            self.panel_retorno.ventana.deiconify()

            self.panel_retorno.ventana.state(
                "zoomed"
            )

    # ======================================
    # CERRAR SESION
    # ======================================

    def cerrar_sesion(self):

        confirmacion = ConfirmacionLogout(
            self.ventana,
            "¿Deseas cerrar sesión?"
        )

        if confirmacion.resultado:

            self.ventana.destroy()

            if self.ventana_padre:

                self.ventana_padre.deiconify()

                self.ventana_padre.state(
                    "zoomed"
                )

    # ======================================
    # CERRAR SISTEMA
    # ======================================

    def cerrar_aplicacion(self):

        confirmacion = ConfirmacionLogout(
            self.ventana,
            "¿Deseas cerrar el sistema?"
        )

        if confirmacion.resultado:

            self.ventana.destroy()

            if self.ventana_padre:

                self.ventana_padre.destroy()