# ==========================================
# ARCHIVO: login_base.py
# ==========================================

import tkinter as tk


class LoginBase:

    def __init__(self, ventana_padre, titulo_login):

        self.ventana_padre = ventana_padre

        # ==================================
        # VENTANA LOGIN
        # ==================================
        self.ventana = tk.Toplevel()

        self.ventana.title(titulo_login)

        # Pantalla completa
        self.ventana.state("zoomed")

        # Tamaño mínimo
        self.ventana.minsize(1200, 700)

        # ==================================
        # COLORES
        # ==================================
        self.COLOR_FONDO = "#8DB9E2"
        self.COLOR_BLANCO = "#F5F5F5"
        self.COLOR_AZUL = "#3D86D6"

        self.ventana.configure(bg=self.COLOR_FONDO)

        # ==================================
        # CERRAR TODO EL SISTEMA
        # ==================================
        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar_sistema
        )

        # ==================================
        # CONTENEDOR CENTRAL
        # ==================================
        self.contenedor = tk.Frame(
            self.ventana,
            bg=self.COLOR_BLANCO
        )

        self.contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ==================================
        # BOTON REGRESAR
        # ==================================
        self.btn_regresar = tk.Button(
            self.ventana,
            text="↩",
            font=("Arial", 30),
            bg=self.COLOR_FONDO,
            fg="white",
            bd=0,
            cursor="hand2",
            activebackground=self.COLOR_FONDO,
            activeforeground="white",
            command=self.cerrar_login
        )

        self.btn_regresar.place(x=20, y=20)

        # ==================================
        # TITULO
        # ==================================
        self.titulo = tk.Label(
            self.contenedor,
            text=titulo_login,
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_AZUL
        )

        self.titulo.pack(
            pady=(60, 70)
        )

        # ==================================
        # USERNAME
        # ==================================
        self.frame_user = tk.Frame(
            self.contenedor,
            bg=self.COLOR_BLANCO
        )

        self.frame_user.pack(
            pady=25,
            padx=80
        )

        self.icon_user = tk.Label(
            self.frame_user,
            text="👤",
            bg=self.COLOR_AZUL,
            fg="white"
        )

        self.icon_user.pack(side="left")

        self.entry_user = tk.Entry(
            self.frame_user,
            bd=1,
            relief="solid",
            width=35
        )

        self.entry_user.pack(
            side="left",
            ipady=18,
            padx=(10, 0)
        )

        # ==================================
        # PASSWORD
        # ==================================
        self.frame_pass = tk.Frame(
            self.contenedor,
            bg=self.COLOR_BLANCO
        )

        self.frame_pass.pack(
            pady=25,
            padx=80
        )

        self.icon_pass = tk.Label(
            self.frame_pass,
            text="🔒",
            bg=self.COLOR_AZUL,
            fg="white"
        )

        self.icon_pass.pack(side="left")

        self.entry_pass = tk.Entry(
            self.frame_pass,
            bd=1,
            relief="solid",
            show="*",
            width=35
        )

        self.entry_pass.pack(
            side="left",
            ipady=18,
            padx=(10, 0)
        )

        # ==================================
        # BOTON LOGIN
        # ==================================
        self.btn_login = tk.Button(
            self.contenedor,
            text="Login",
            bg=self.COLOR_AZUL,
            fg="white",
            bd=0,
            cursor="hand2",
            command=self.login
        )

        self.btn_login.pack(
            pady=70,
            ipadx=170,
            ipady=15
        )

        # ==================================
        # RESPONSIVE
        # ==================================
        self.ventana.bind(
            "<Configure>",
            self.responsive
        )

        self.responsive()

    # ======================================
    # RESPONSIVE
    # ======================================
    def responsive(self, event=None):

        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        # ==================================
        # PANEL CENTRAL
        # ==================================
        panel_ancho = int(ancho * 0.50)
        panel_alto = int(alto * 0.72)

        if panel_ancho < 850:
            panel_ancho = 850

        if panel_alto < 650:
            panel_alto = 650

        self.contenedor.config(
            width=panel_ancho,
            height=panel_alto
        )

        # ==================================
        # TAMAÑOS
        # ==================================
        titulo_size = int(ancho * 0.022)
        texto_size = int(ancho * 0.011)
        icono_size = int(ancho * 0.018)

        if titulo_size < 28:
            titulo_size = 28

        if texto_size < 16:
            texto_size = 16

        if icono_size < 24:
            icono_size = 24

        # ==================================
        # TITULO
        # ==================================
        self.titulo.config(
            font=("Arial", titulo_size, "bold")
        )

        # ==================================
        # ICONOS
        # ==================================
        self.icon_user.config(
            font=("Arial", icono_size),
            width=4,
            height=2
        )

        self.icon_pass.config(
            font=("Arial", icono_size),
            width=4,
            height=2
        )

        # ==================================
        # INPUTS
        # ==================================
        self.entry_user.config(
            font=("Arial", texto_size)
        )

        self.entry_pass.config(
            font=("Arial", texto_size)
        )

        # ==================================
        # BOTON LOGIN
        # ==================================
        self.btn_login.config(
            font=("Arial", texto_size + 3)
        )

    # ======================================
    # LOGIN
    # ======================================
    def login(self):

        usuario = self.entry_user.get()
        password = self.entry_pass.get()

        print(usuario)
        print(password)

    # ======================================
    # REGRESAR
    # ======================================
    def cerrar_login(self):

        self.ventana.destroy()

        self.ventana_padre.deiconify()

        self.ventana_padre.state("zoomed")

    # ======================================
    # CERRAR TODO EL SISTEMA
    # ======================================
    def cerrar_sistema(self):

        self.ventana.destroy()

        self.ventana_padre.destroy()

        exit()