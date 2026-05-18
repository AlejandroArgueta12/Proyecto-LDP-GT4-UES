# ==========================================
# ARCHIVO: login_trabajador.py
# ==========================================

import json
import os
from tkinter import messagebox

from login_base import LoginBase
from panel_trabajador import PanelTrabajador


# ==========================================
# RUTA DEL JSON
# ==========================================

RUTA_JSON = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "usuarios.json"
)

RUTA_JSON = os.path.abspath(RUTA_JSON)


# ==========================================
# CLASE LOGIN TRABAJADOR
# ==========================================

class LoginTrabajador(LoginBase):

    def __init__(self, ventana_padre):

        super().__init__(
            ventana_padre,
            "Login de Trabajador"
        )

    # ==========================================
    # LOGIN
    # ==========================================

    def login(self):

        usuario = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        # ==========================================
        # VALIDAR CAMPOS
        # ==========================================

        if usuario == "" or password == "":

            messagebox.showwarning(
                "Advertencia",
                "Complete todos los campos"
            )

            return

        # ==========================================
        # LEER JSON
        # ==========================================

        try:

            with open(
                RUTA_JSON,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "No se encontró el archivo usuarios.json"
            )

            return

        except json.JSONDecodeError:

            messagebox.showerror(
                "Error",
                "El archivo JSON está dañado"
            )

            return

        # ==========================================
        # OBTENER EMPLEADOS
        # ==========================================

        empleados = datos.get(
            "empleados",
            []
        )

        acceso = False

        # ==========================================
        # VALIDAR USUARIO
        # ==========================================

        for empleado in empleados:

            if (
                empleado["usuario"] == usuario
                and
                empleado["password"] == password
            ):

                acceso = True
                break

        # ==========================================
        # ACCESO CORRECTO
        # ==========================================

        if acceso:

            messagebox.showinfo(
                "Correcto",
                "Bienvenido trabajador"
            )

            # OCULTAR VENTANA PRINCIPAL
            self.ventana_padre.withdraw()

            # CERRAR LOGIN
            self.ventana.destroy()

            # ABRIR PANEL TRABAJADOR
            PanelTrabajador(
                self.ventana_padre
            )

        # ==========================================
        # ACCESO INCORRECTO
        # ==========================================

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )