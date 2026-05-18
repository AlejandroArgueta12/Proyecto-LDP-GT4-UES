# ==========================================
# ARCHIVO: panel_admin.py
# ==========================================

from panel_base import PanelBase


class PanelAdmin(PanelBase):

    def __init__(self, ventana_padre):

        botones = [

            ("Creación", True),

            ("Asignación", True),

            ("Ver informes", True)
        ]

        super().__init__(
            "Administrador",
            botones,
            "admin",
            ventana_padre
        )