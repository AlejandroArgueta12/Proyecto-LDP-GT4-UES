# ==========================================
# ARCHIVO: seleccionar_usuario.py
# ==========================================

import tkinter as tk
import sys

from login_admin import LoginAdmin
from login_trabajador import LoginTrabajador

# ==========================================
# VENTANA PRINCIPAL
# ==========================================
ventana = tk.Tk()

ventana.title("Seleccionar Usuario")

# Pantalla completa
ventana.state("zoomed")

# Tamaño mínimo
ventana.minsize(1200, 700)

# ==========================================
# COLORES
# ==========================================
COLOR_FONDO = "#8DB9E2"
COLOR_BLANCO = "#F5F5F5"
COLOR_AZUL = "#3D86D6"

ventana.configure(bg=COLOR_FONDO)

# ==========================================
# CERRAR TODO EL SISTEMA
# ==========================================
def cerrar_sistema():

    ventana.destroy()

    sys.exit()

# Evento al presionar X
ventana.protocol(
    "WM_DELETE_WINDOW",
    cerrar_sistema
)

# ==========================================
# CONTENEDOR CENTRAL
# ==========================================
contenedor = tk.Frame(
    ventana,
    bg=COLOR_BLANCO
)

contenedor.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

# ==========================================
# ABRIR LOGIN ADMIN
# ==========================================
def abrir_admin():

    ventana.withdraw()

    LoginAdmin(ventana)

# ==========================================
# ABRIR LOGIN TRABAJADOR
# ==========================================
def abrir_trabajador():

    ventana.withdraw()

    LoginTrabajador(ventana)

# ==========================================
# TITULO
# ==========================================
titulo = tk.Label(
    contenedor,
    text="Seleccione su usuario",
    bg=COLOR_BLANCO,
    fg=COLOR_AZUL
)

titulo.pack(
    pady=(60, 70)
)

# ==========================================
# ADMIN
# ==========================================
frame_admin = tk.Frame(
    contenedor,
    bg=COLOR_BLANCO
)

frame_admin.pack(
    pady=25,
    padx=80
)

icono_admin = tk.Label(
    frame_admin,
    text="⚙",
    bg=COLOR_AZUL,
    fg="white"
)

icono_admin.pack(side="left")

btn_admin = tk.Button(
    frame_admin,
    text="Administrador",
    bg="white",
    fg="#2563EB",
    relief="solid",
    bd=1,
    cursor="hand2",
    command=abrir_admin
)

btn_admin.pack(
    side="left",
    ipady=18,
    ipadx=90,
    padx=(10, 0)
)

# ==========================================
# TRABAJADOR
# ==========================================
frame_trabajador = tk.Frame(
    contenedor,
    bg=COLOR_BLANCO
)

frame_trabajador.pack(
    pady=25,
    padx=80
)

icono_trabajador = tk.Label(
    frame_trabajador,
    text="💼",
    bg=COLOR_AZUL,
    fg="white"
)

icono_trabajador.pack(side="left")

btn_trabajador = tk.Button(
    frame_trabajador,
    text="Trabajador",
    bg="white",
    fg="#2563EB",
    relief="solid",
    bd=1,
    cursor="hand2",
    command=abrir_trabajador
)

btn_trabajador.pack(
    side="left",
    ipady=18,
    ipadx=110,
    padx=(10, 0)
)

# ==========================================
# RESPONSIVE
# ==========================================
def responsive(event=None):

    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()

    # ======================================
    # PANEL CENTRAL
    # ======================================
    panel_ancho = int(ancho * 0.50)
    panel_alto = int(alto * 0.65)

    if panel_ancho < 850:
        panel_ancho = 850

    if panel_alto < 550:
        panel_alto = 550

    contenedor.config(
        width=panel_ancho,
        height=panel_alto
    )

    # ======================================
    # TAMAÑOS
    # ======================================
    titulo_size = int(ancho * 0.022)
    boton_size = int(ancho * 0.011)
    icono_size = int(ancho * 0.018)

    if titulo_size < 28:
        titulo_size = 28

    if boton_size < 16:
        boton_size = 16

    if icono_size < 24:
        icono_size = 24

    # ======================================
    # TITULO
    # ======================================
    titulo.config(
        font=("Arial", titulo_size, "bold")
    )

    # ======================================
    # ICONOS
    # ======================================
    icono_admin.config(
        font=("Arial", icono_size),
        width=4,
        height=2
    )

    icono_trabajador.config(
        font=("Arial", icono_size),
        width=4,
        height=2
    )

    # ======================================
    # BOTONES
    # ======================================
    btn_admin.config(
        font=("Arial", boton_size)
    )

    btn_trabajador.config(
        font=("Arial", boton_size)
    )

# ==========================================
# RESPONSIVE
# ==========================================
ventana.bind(
    "<Configure>",
    responsive
)

responsive()

# ==========================================
# MAINLOOP
# ==========================================
ventana.mainloop()