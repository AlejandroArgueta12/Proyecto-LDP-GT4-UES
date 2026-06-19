# ==========================================
# ARCHIVO: panel_trabajador.py
# ==========================================
from panel_base import PanelBase

class PanelTrabajador(PanelBase):

    def __init__(self, ventana_padre):

        # Definimos los botones. Para el trabajador, "Creación" se queda deshabilitado (False)
        botones = [
            ("Creación", False),
            ("Asignación", True),   # Habilitamos para que pueda registrar sus horas
            ("Ver informes", True)  # Habilitamos para que pueda ver la tabla de reportes
        ]

        super().__init__(
            "Trabajador",
            botones,
            "trabajador",
            ventana_padre
        )

        # ======================================
        # ENLAZAR BOTONES A SUS FUNCIONES
        # ======================================
        # El botón [0] (Creación) está deshabilitado, así que no le asignamos comando
        self.botones_menu[1].config(command=self.abrir_asignacion_horas)
        self.botones_menu[2].config(command=self.abrir_informes)

    # ======================================
    # FUNCIONES PARA ABRIR PANTALLAS DIRECTAS
    # ======================================
    def abrir_asignacion_horas(self):
        # En lugar de mandarlo al menú de asignación de proyectos/trabajadores, lo mandamos directamentea la pantalla de ingresar horas.
        from asignar_horas_trabajadas import AsignarHorasTrabajadas
        self.ventana.withdraw()
        # Le pasamos "self" como panel de retorno para que al darle "Retroceder" regrese aquí
        AsignarHorasTrabajadas(self.ventana_padre, self)

    def abrir_informes(self):
        from ver_informes import VerInformes
        self.ventana.withdraw()
        VerInformes(self.ventana_padre, self)