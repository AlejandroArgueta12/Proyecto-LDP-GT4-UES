# ==========================================
# ARCHIVO: panel_trabajador.py
# ==========================================

from panel_base import PanelBase


class PanelTrabajador(PanelBase):

    def __init__(self, ventana_padre):

        botones = [

            ("Creación", False),

            ("Asignación", False),

            ("Ver informes", True)
        ]

        super().__init__(
            "Trabajador",
            botones,
            "trabajador",
            ventana_padre
        )