# ==========================================
# ARCHIVO: test_sistema.py
# ==========================================

import unittest
import os
import json

# Importamos el controlador de la base de datos de la interfaz gráfica.
import controlador_datos as db

class TestGestorProyectos(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial: 
        Crea un respaldo temporal de la base de datos y carga datos de prueba limpios.
        """
        self.backup_bd = {}
        if os.path.exists(db.RUTA_BD):
            with open(db.RUTA_BD, "r", encoding="utf-8") as f:
                self.backup_bd = json.load(f)
        
        # Inyectamos los datos de prueba controlados
        datos_prueba = {
            "empleados":{
                "EMP-TEST" :{"nombre": "Empleado de Prueba", "cargo": "Tester", "registro_horas_diarias": {}}
            },
            "proyectos": {
                "PRJ-TEST": {"nombre": "Proyecto Prueba", "fecha_inicio": "01/01/2026", "fecha_fin": "31/12/2026", "tareas": [], "empleados_asignados": []}
            },
            "tareas": {
                "TAR-TEST": {"nombre_tarea": "Test Unitario", "descripcion": "Prueba de sistema", "horas_invertidas": 0, "proyecto_asignado": "PRJ-TEST", "empleado_asignado": "EMP-TEST"}
            }
        }
        db.guardar_datos(datos_prueba)
    
    def tearDown(self):
        """
        Restauración: 
        Devuelve la base de datos a su estado original después de cada prueba.
        """
        if self.backup_bd:
            db.guardar_datos(self.backup_bd)
        elif os.path.exists(db.RUTA_BD):
            os.remove(db.RUTA_BD)

# ==========================================
# PRUEBA 1
# ==========================================
    def test_validacion_jornada_maxima(self):
        """
        Prueba que el sistema rechaza el registro de más de 24 horas en un mismo día.
        """
        # Se registran 10 horas válidas
        exito1, msj1 = db.registrar_horas_tarea("TAR-TEST", 10.0, "20/06/2026")
        self.assertTrue(exito1, "Fallo al registrar las primeras 10 horas válidas.")
        
        # Se intenta registrar 15 horas más el mismo día (Total: 25h -> Debe fallar)
        exito2, msj2 = db.registrar_horas_tarea("TAR-TEST", 15.0, "20/06/2026")
        self.assertFalse(exito2, "El sistema permitió registrar una jornada mayor a 24 horas.")
        self.assertIn("Jornada irreal", msj2, "El mensaje de error no coincide con la validación esperada.")

if __name__ == "__main__":
    unittest.main()
