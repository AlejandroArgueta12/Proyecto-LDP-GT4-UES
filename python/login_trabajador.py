# ==========================================
# ARCHIVO: login_trabajador.py
# ==========================================

import json
import os
from tkinter import messagebox
from login_base import LoginBase


RUTA_JSON = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "usuarios.json"
)

RUTA_JSON = os.path.abspath(RUTA_JSON)


class LoginTrabajador(LoginBase):

    def __init__(self, ventana_padre):

        super().__init__(
            ventana_padre,
            "Login de Trabajador"
        )

    def login(self):

        usuario = self.entry_user.get()
        password = self.entry_pass.get()

        with open(RUTA_JSON, "r") as archivo:

            datos = json.load(archivo)

        empleados = datos["empleados"]

        acceso = False

        for empleado in empleados:

            if (
                empleado["usuario"] == usuario
                and
                empleado["password"] == password
            ):

                acceso = True
                break

        if acceso:

            messagebox.showinfo(
                "Correcto",
                "Bienvenido trabajador"
            )

            print("TRABAJADOR")
            print(usuario)

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )