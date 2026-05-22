# ==========================================
# ARCHIVO: panel_base.py
# ==========================================

import tkinter as tk

from PIL import Image, ImageTk

from confirmacion_logout import ConfirmacionLogout


class PanelBase:

    def __init__(
        self,
        titulo,
        botones,
        login_callback=None,
        ventana_padre=None
    ):

        # LOGIN
        self.login_callback = login_callback

        # VENTANA PADRE
        self.ventana_padre = ventana_padre

        # ======================================
        # VENTANA
        # ======================================

        self.ventana = tk.Toplevel()

        self.ventana.title(titulo)

        # VENTANA MAXIMIZADA
        self.ventana.state("zoomed")

        # TAMAÑO MINIMO
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
        self.COLOR_FONDO = "white"

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
            bg=self.COLOR_BARRA
        )

        self.barra.pack(
            side="top",
            fill="x"
        )

        # ======================================
        # TITULO
        # ======================================

        self.texto_titulo = tk.Label(
            self.barra,
            text="👤 " + titulo,
            bg=self.COLOR_BARRA,
            fg=self.COLOR_TEXTO,
            font=("Arial", 20, "bold")
        )

        self.texto_titulo.place(
            relx=0.03,
            rely=0.5,
            anchor="w"
        )

        # ======================================
        # BOTON CERRAR SESION
        # ======================================

        self.btn_cerrar = tk.Button(
            self.barra,
            text="❌ Cerrar Sesión",
            bg=self.COLOR_BARRA,
            fg=self.COLOR_TEXTO,
            bd=2,
            relief="solid",
            cursor="hand2",
            command=self.cerrar_sesion
        )

        self.btn_cerrar.place(
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
        # MENU
        # ======================================

        self.menu = tk.Frame(
            self.principal,
            bg=self.COLOR_MENU
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

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
        # ICONOS
        # ======================================

        self.iconos = {
            "creación": "➕",
            "asignación": "📋",
            "informe": "📊"
        }

        # ======================================
        # BOTONES MENU
        # ======================================

        self.botones_menu = []

        for texto, habilitado in botones:

            texto_con_icono = texto

            for clave, icono in self.iconos.items():

                if clave in texto.lower():

                    texto_con_icono = f"{icono}  {texto}"
                    break

            boton = tk.Button(
                self.menu,
                text=texto_con_icono,
                bd=2,
                cursor="hand2",
                anchor="w",
                padx=15
            )

            if habilitado:

                boton.config(
                    bg=self.COLOR_MENU,
                    fg=self.COLOR_TEXTO,
                    activebackground=self.COLOR_MENU,
                    activeforeground=self.COLOR_TEXTO
                )

            else:

                boton.config(
                    state="disabled"
                )

            boton.pack(
                pady=35,
                padx=20,
                fill="x"
            )

            self.botones_menu.append(boton)

        # ======================================
        # IMAGEN
        # ======================================

        self.label_imagen = tk.Label(
            self.contenido,
            bg=self.COLOR_FONDO
        )

        self.label_imagen.place(
            relx=0.5,
            rely=0.42,
            anchor="center"
        )

        # ======================================
        # RUTA IMAGEN
        # ======================================

        self.RUTA_IMAGEN = "assets/img/21430-scaled-e1614339566329.jpg"

        # ======================================
        # TEXTO BIENVENIDA
        # ======================================

        self.bienvenida = tk.Label(
            self.contenido,
            text="Bienvenido al sistema de Gestión de proyectos",
            bg=self.COLOR_FONDO,
            fg="black",
            font=("Arial", 18, "bold")
        )

        self.bienvenida.place(
            relx=0.5,
            rely=0.78,
            anchor="center"
        )

        # ======================================
        # RESPONSIVE
        # ======================================

        self.ventana.bind(
            "<Configure>",
            self.responsive
        )

        self.responsive()

    # ======================================
    # CARGAR IMAGEN
    # ======================================

    def cargar_imagen(self, ancho):

        try:

            imagen = Image.open(
                self.RUTA_IMAGEN
            )

            tamaño = int(ancho * 0.22)

            if tamaño < 180:
                tamaño = 180

            imagen = imagen.resize(
                (tamaño, tamaño)
            )

            self.imagen_tk = ImageTk.PhotoImage(
                imagen
            )

            self.label_imagen.config(
                image=self.imagen_tk
            )

        except:

            self.label_imagen.config(
                text="No se pudo cargar la imagen",
                font=("Arial", 16),
                fg="red"
            )

    # ======================================
    # CERRAR SESION
    # ======================================

    def cerrar_sesion(self):

        confirmacion = ConfirmacionLogout(
            self.ventana,
            "¿Estás seguro que quieres cerrar sesión?"
        )

        if confirmacion.resultado:

            self.ventana.destroy()

            self.ventana_padre.deiconify()

            self.ventana_padre.state("zoomed")

    # ======================================
    # CERRAR TODO EL SISTEMA
    # ======================================

    def cerrar_aplicacion(self):

        confirmacion = ConfirmacionLogout(
            self.ventana,
            "¿Estás seguro que quieres cerrar el sistema por completo?"
        )

        if confirmacion.resultado:

            self.ventana.destroy()

            self.ventana_padre.destroy()

    # ======================================
    # RESPONSIVE
    # ======================================

    def responsive(self, event=None):

        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        barra_alto = max(int(alto * 0.09), 70)

        menu_ancho = max(int(ancho * 0.18), 220)

        titulo_size = max(int(ancho * 0.015), 18)

        texto_size = max(int(ancho * 0.010), 14)

        boton_size = max(int(ancho * 0.010), 13)

        self.barra.config(
            height=barra_alto
        )

        self.menu.config(
            width=menu_ancho
        )

        self.texto_titulo.config(
            font=("Arial", titulo_size, "bold")
        )

        self.btn_cerrar.config(
            font=("Arial", boton_size, "bold"),
            padx=15,
            pady=8
        )

        for boton in self.botones_menu:

            boton.config(
                font=("Arial", boton_size + 2),
                pady=12
            )

        self.bienvenida.config(
            font=("Arial", texto_size + 4, "bold")
        )

        # ACTUALIZAR IMAGEN
        self.cargar_imagen(ancho)