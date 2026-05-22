# ==========================================
# ARCHIVO: controlador_datos.py
# ==========================================
import json
import os

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "..", "data", "base_datos.json")
RUTA_BD = os.path.abspath(RUTA_BD)

def cargar_datos():
    if not os.path.exists(RUTA_BD):
        return {"empleados": {}, "proyectos": {}, "tareas": {}}
    try:
        with open(RUTA_BD, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"empleados": {}, "proyectos": {}, "tareas": {}}

def guardar_datos(datos):
    os.makedirs(os.path.dirname(RUTA_BD), exist_ok=True)
    with open(RUTA_BD, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# --- CREACIÓN ---
def registrar_empleado(id_emp, nombres, apellidos, cargo):
    datos = cargar_datos()
    if id_emp in datos.get("empleados", {}):
        return False, "El ID del trabajador ya existe."
    
    # Se unifican los campos para conservar la compatibilidad de lectura
    nombre_completo = f"{nombres} {apellidos}".strip()
    
    datos.setdefault("empleados", {})[id_emp] = {
        "nombre": nombre_completo,
        "cargo": cargo,
        "registro_horas_diarias": {}
    }
    guardar_datos(datos)
    return True, "Trabajador registrado con éxito."

def registrar_proyecto(id_proj, nombre, fecha_inicio, fecha_fin):
    datos = cargar_datos()
    if id_proj in datos.get("proyectos", {}):
        return False, "El ID del proyecto ya existe."
    
    datos.setdefault("proyectos", {})[id_proj] = {
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "tareas": [],
        "empleados_asignados": []
    }
    guardar_datos(datos)
    return True, "Proyecto registrado con éxito."

def registrar_tarea(id_tarea, nombre, descripcion):
    datos = cargar_datos()
    if id_tarea in datos.get("tareas", {}):
        return False, "El ID de la tarea ya existe."
    
    datos.setdefault("tareas", {})[id_tarea] = {
        "nombre_tarea": nombre,
        "descripcion": descripcion,
        "horas_invertidas": 0,
        "proyecto_asignado": None,
        "empleado_asignado": "SIN ASIGNAR"
    }
    guardar_datos(datos)
    return True, "Tarea registrada con éxito."

# --- REPORTES ---
def obtener_reporte_tareas():
    datos = cargar_datos()
    lista_reporte = []

    # 1. Extraer tareas creadas desde la Interfaz Gráfica
    for id_t, info in datos.get("tareas", {}).items():
        lista_reporte.append((
            id_t, 
            info.get("nombre_tarea", "Sin nombre"), 
            info.get("proyecto_asignado", "Sin asignar"), 
            info.get("empleado_asignado", "Sin asignar"), 
            info.get("horas_invertidas", 0)
        ))

    # 2. Extraer tareas creadas desde la Consola
    for id_proj, info_proj in datos.get("proyectos", {}).items():
        tareas_consola = info_proj.get("tareas", [])
        for indice, tarea in enumerate(tareas_consola):
            # La consola no solicitaba ID de tarea, así que generamos uno visual
            id_generado = f"{id_proj}-T{indice + 1}"
            lista_reporte.append((
                id_generado,
                tarea.get("nombre_tarea", "Sin nombre"),
                id_proj,
                tarea.get("empleado_asignado", "Sin asignar"),
                tarea.get("horas_invertidas", 0)
            ))

    return lista_reporte

def obtener_reporte_empleados():
    datos = cargar_datos()
    lista_reporte = []
    for id_emp, info in datos.get("empleados", {}).items():
        lista_reporte.append((
            id_emp, 
            info.get("nombre", "Sin nombre"), 
            info.get("cargo", "Sin cargo")
        ))
    return lista_reporte

def obtener_reporte_proyectos():
    datos = cargar_datos()
    lista_reporte = []
    for id_proj, info in datos.get("proyectos", {}).items():
        lista_reporte.append((
            id_proj, 
            info.get("nombre", "Sin nombre"), 
            info.get("fecha_inicio", "N/A"), 
            info.get("fecha_fin", "N/A")
        ))
    return lista_reporte

# --- GESTIÓN ---
def obtener_entidad(tipo, id_entidad):
    datos = cargar_datos()
    return datos.get(tipo, {}).get(id_entidad, None)

def actualizar_entidad(tipo, id_entidad, nuevos_datos):
    datos = cargar_datos()
    if id_entidad in datos.get(tipo, {}):
        for clave, valor in nuevos_datos.items():
            datos[tipo][id_entidad][clave] = valor
        guardar_datos(datos)
        return True, "Datos actualizados con éxito."
    return False, "El ID no existe."

def eliminar_entidad(tipo, id_entidad):
    datos = cargar_datos()
    if id_entidad in datos.get(tipo, {}):
        del datos[tipo][id_entidad]
        guardar_datos(datos)
        return True, "Registro eliminado con éxito."
    return False, "El ID no existe."

# --- ASIGNACIONES ---
def asignar_tarea_proyecto(id_tarea, id_proyecto):
    datos = cargar_datos()
    if id_tarea not in datos.get("tareas", {}):
        return False, "La tarea no existe."
    if id_proyecto not in datos.get("proyectos", {}):
        return False, "El proyecto no existe."
    
    datos["tareas"][id_tarea]["proyecto_asignado"] = id_proyecto
    guardar_datos(datos)
    return True, "Tarea asignada al proyecto con éxito."

def asignar_tarea_trabajador(id_tarea, id_trabajador):
    datos = cargar_datos()
    if id_tarea not in datos.get("tareas", {}):
        return False, "La tarea no existe."
    if id_trabajador not in datos.get("empleados", {}):
        return False, "El trabajador no existe."
    
    datos["tareas"][id_tarea]["empleado_asignado"] = id_trabajador
    guardar_datos(datos)
    return True, "Tarea asignada al trabajador con éxito."

def registrar_horas_tarea(id_tarea, horas, fecha):
    datos = cargar_datos()
    
    if id_tarea not in datos.get("tareas", {}):
        return False, "La tarea no existe."
        
    tarea = datos["tareas"][id_tarea]
    id_empleado = tarea.get("empleado_asignado", "SIN ASIGNAR")

    if id_empleado == "SIN ASIGNAR" or id_empleado not in datos.get("empleados", {}):
        return False, "Debe asignar un trabajador a esta tarea primero."

    try:
        horas_float = float(horas)
        if horas_float <= 0:
            return False, "La cantidad de horas debe ser mayor a 0."
    except ValueError:
        return False, "Ingrese un valor numérico para las horas."

    # Validación de las 24 horas diarias en el perfil del empleado
    empleado = datos["empleados"][id_empleado]
    # Asegurarnos de que el diccionario de registro diario exista
    registro_diario = empleado.setdefault("registro_horas_diarias", {})
    
    # Obtener horas ya trabajadas ese día
    horas_ya_registradas = float(registro_diario.get(fecha, 0.0))

    if horas_ya_registradas + horas_float > 24:
        return False, f"Jornada irreal. El empleado {id_empleado} ya tiene {horas_ya_registradas}h registradas el {fecha}."

    # Guardar en el perfil del empleado
    registro_diario[fecha] = horas_ya_registradas + horas_float
    
    # Sumar al total histórico de la tarea
    tarea["horas_invertidas"] = tarea.get("horas_invertidas", 0) + horas_float

    guardar_datos(datos)
    return True, f"Se registraron {horas_float}h correctamente."