# ==========================================
# ARCHIVO: test_sistema.py
# ==========================================

import unittest
import os
import json

# Importamos el controlador de datos
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

        # Datos de prueba controlados
        datos_prueba = {
            "empleados": {
                "EMP-TEST": {
                    "nombre": "Empleado de Prueba",
                    "cargo": "Tester",
                    "registro_horas_diarias": {}
                }
            },
            "proyectos": {
                "PRJ-TEST": {
                    "nombre": "Proyecto Prueba",
                    "fecha_inicio": "01/01/2026",
                    "fecha_fin": "31/12/2026",
                    "tareas": [],
                    "empleados_asignados": []
                }
            },
            "tareas": {
                "TAR-TEST": {
                    "nombre_tarea": "Test Unitario",
                    "descripcion": "Prueba de sistema",
                    "horas_invertidas": 0,
                    "proyecto_asignado": "PRJ-TEST",
                    "empleado_asignado": "EMP-TEST"
                }
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

        exito1, msj1 = db.registrar_horas_tarea(
            "TAR-TEST",
            10.0,
            "20/06/2026"
        )

        self.assertTrue(
            exito1,
            "Fallo al registrar las primeras 10 horas válidas."
        )

        exito2, msj2 = db.registrar_horas_tarea(
            "TAR-TEST",
            15.0,
            "20/06/2026"
        )

        self.assertFalse(
            exito2,
            "El sistema permitió registrar una jornada mayor a 24 horas."
        )

        self.assertIn(
            "Jornada irreal",
            msj2,
            "El mensaje de error no coincide con la validación esperada."
        )

    # ==========================================
    # PRUEBA 2
    # ==========================================
    def test_integridad_id_duplicado(self):
        """
        Prueba que el sistema no permita sobrescribir o duplicar el ID de un empleado existente.
        """

        exito, msj = db.registrar_empleado(
            "EMP-TEST",
            "Nuevo",
            "Usuario",
            "Desarrollador"
        )

        self.assertFalse(
            exito,
            "El sistema permitió registrar un empleado con un ID ya existente."
        )

        self.assertEqual(
            msj,
            "El ID del trabajador ya existe.",
            "El mensaje de error de duplicidad es incorrecto."
        )

    # ==========================================
    # PRUEBA 3
    # ==========================================
    def test_registro_horas_tarea_inexistente(self):
        """
        Prueba que el sistema no permita registrar horas en una tarea inexistente.
        """

        exito, msj = db.registrar_horas_tarea(
            "TAR-NOEXISTE",
            5,
            "20/06/2026"
        )

        self.assertFalse(
            exito,
            "El sistema permitió registrar horas en una tarea inexistente."
        )

        self.assertEqual(
            msj,
            "La tarea no existe.",
            "El mensaje para tarea inexistente es incorrecto."
        )

    # ==========================================
    # PRUEBA 4
    # ==========================================
    def test_registro_horas_valido(self):
        """
        Prueba que el sistema permita registrar horas válidas.
        """

        exito, msj = db.registrar_horas_tarea(
            "TAR-TEST",
            8,
            "20/06/2026"
        )

        self.assertTrue(
            exito,
            "El sistema rechazó un registro válido de horas."
        )

        self.assertIn(
            "Se registraron",
            msj,
            "No se registraron correctamente las horas válidas."
        )

    # ==========================================
    # PRUEBA 5
    # ==========================================
    def test_horas_negativas(self):
        """
        Prueba que el sistema rechace horas negativas.
        """

        exito, msj = db.registrar_horas_tarea(
            "TAR-TEST",
            -5,
            "20/06/2026"
        )

        self.assertFalse(
            exito,
            "El sistema permitió registrar horas negativas."
        )

        self.assertEqual(
            msj,
            "La cantidad de horas debe ser mayor a 0.",
            "El mensaje para horas negativas es incorrecto."
        )

    # ==========================================
    # PRUEBA 6
    # ==========================================
    def test_horas_no_numericas(self):
        """
        Prueba que el sistema rechace valores no numéricos.
        """

        exito, msj = db.registrar_horas_tarea(
            "TAR-TEST",
            "ABC",
            "20/06/2026"
        )

        self.assertFalse(
            exito,
            "El sistema permitió registrar un valor no numérico."
        )

        self.assertEqual(
            msj,
            "Ingrese un valor numérico para las horas.",
            "El mensaje para horas no numéricas es incorrecto."
        )


if __name__ == "__main__":
    unittest.main()