# ==========================================
# ARCHIVO: panel_admin.py
# ==========================================
from panel_base import PanelBase

class PanelAdmin(PanelBase):

    def __init__(self, ventana_padre):

        botones = [
            ("Creación", True),
            ("Asignación", True),
            ("Gestión de datos", True),
            ("Ver informes", True)
        ]

        super().__init__(
            "Administrador",
            botones,
            "admin",
            ventana_padre
        )

        self.botones_menu[0].config(command=self.abrir_crear_proyecto)
        self.botones_menu[1].config(command=self.abrir_asignacion)
        self.botones_menu[2].config(command=self.abrir_gestion)
        self.botones_menu[3].config(command=self.abrir_informes)

    def abrir_crear_proyecto(self):
        from crear_proyecto import CrearProyecto
        self.ventana.withdraw()
        CrearProyecto(self.ventana_padre, self)

    def abrir_asignacion(self):
        from asignar_tarea_a_proyecto import AsignarTareaAProyecto
        self.ventana.withdraw()
        AsignarTareaAProyecto(self.ventana_padre, self)

    def abrir_gestion(self):
        from gestionar_datos import GestionarDatos
        self.ventana.withdraw()
        GestionarDatos(self.ventana_padre, self)

    def abrir_informes(self):
        from ver_informes import VerInformes
        self.ventana.withdraw()
        VerInformes(self.ventana_padre, self)