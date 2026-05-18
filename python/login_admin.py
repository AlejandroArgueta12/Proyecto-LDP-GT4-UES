# ==========================================
# ARCHIVO: login_admin.py
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

class LoginAdmin(LoginBase):

    def __init__(self, ventana_padre):

        super().__init__(
            ventana_padre,
            "Login de Administrador"
        )

    def login(self):

        usuario = self.entry_user.get()
        password = self.entry_pass.get()

        with open(RUTA_JSON, "r") as archivo:

            datos = json.load(archivo)

        admins = datos["admins"]

        acceso = False

        for admin in admins:

            if (
                admin["usuario"] == usuario
                and
                admin["password"] == password
            ):

                acceso = True
                break

        if acceso:

            messagebox.showinfo(
                "Correcto",
                "Bienvenido administrador"
            )

            print("ADMINISTRADOR")
            print(usuario)

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )