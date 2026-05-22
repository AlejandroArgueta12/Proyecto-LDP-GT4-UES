# ==========================================
# ARCHIVO: panel_admin.py
# ==========================================

from panel_base import PanelBase

from crear_proyecto import CrearProyecto
from asignar_tarea_a_proyecto import AsignarTareaAProyecto


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

        # ======================================
        # BOTON CREACION
        # ======================================

        self.botones_menu[0].config(
            command=self.abrir_crear_proyecto
        )

        # ======================================
        # BOTON ASIGNACION
        # ======================================

        self.botones_menu[1].config(
            command=self.abrir_asignacion
        )

    # ======================================
    # ABRIR CREAR PROYECTO
    # ======================================

    def abrir_crear_proyecto(self):

        self.ventana.withdraw()

        CrearProyecto(
            self.ventana_padre,
            self
        )

    # ======================================
    # ABRIR ASIGNACION
    # ======================================

    def abrir_asignacion(self):

        self.ventana.withdraw()

        AsignarTareaAProyecto(
            self.ventana_padre,
            self
        )