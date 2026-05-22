# ==========================================
# ARCHIVO: confirmacion_logout.py
# ==========================================

import tkinter as tk


class ConfirmacionLogout:

    def __init__(self, ventana_padre, mensaje):

        self.resultado = False

        # ==================================
        # VENTANA
        # ==================================

        self.ventana = tk.Toplevel(
            ventana_padre
        )

        self.ventana.title(
            "Confirmación"
        )

        self.ventana.geometry(
            "500x230"
        )

        self.ventana.resizable(
            False,
            False
        )

        self.ventana.configure(
            bg="white"
        )

        # CENTRAR
        self.centrar_ventana()

        # BLOQUEAR OTRAS VENTANAS
        self.ventana.grab_set()

        # ==================================
        # TEXTO
        # ==================================

        self.label = tk.Label(
            self.ventana,
            text=mensaje,
            font=("Arial", 16, "bold"),
            bg="white",
            fg="black",
            wraplength=420,
            justify="center"
        )

        self.label.pack(
            pady=(45, 30),
            padx=20
        )

        # ==================================
        # FRAME BOTONES
        # ==================================

        self.frame_botones = tk.Frame(
            self.ventana,
            bg="white"
        )

        self.frame_botones.pack()

        # ==================================
        # BOTON SI
        # ==================================

        self.btn_si = tk.Button(
            self.frame_botones,
            text="Sí",
            font=("Arial", 14, "bold"),
            bg="#1f567d",
            fg="white",
            width=10,
            cursor="hand2",
            command=self.confirmar
        )

        self.btn_si.pack(
            side="left",
            padx=15
        )

        # ==================================
        # BOTON NO
        # ==================================

        self.btn_no = tk.Button(
            self.frame_botones,
            text="No",
            font=("Arial", 14, "bold"),
            bg="#b22222",
            fg="white",
            width=10,
            cursor="hand2",
            command=self.cancelar
        )

        self.btn_no.pack(
            side="left",
            padx=15
        )

        # ESPERAR RESPUESTA
        self.ventana.wait_window()

    # ======================================
    # CENTRAR VENTANA
    # ======================================

    def centrar_ventana(self):

        self.ventana.update_idletasks()

        ancho = 500
        alto = 230

        x = (
            self.ventana.winfo_screenwidth() // 2
        ) - (ancho // 2)

        y = (
            self.ventana.winfo_screenheight() // 2
        ) - (alto // 2)

        self.ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )

    # ======================================
    # CONFIRMAR
    # ======================================

    def confirmar(self):

        self.resultado = True

        self.ventana.destroy()

    # ======================================
    # CANCELAR
    # ======================================

    def cancelar(self):

        self.resultado = False

        self.ventana.destroy()