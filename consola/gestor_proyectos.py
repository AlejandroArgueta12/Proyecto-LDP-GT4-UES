
import json
import os
from datetime import datetime
from time import strptime

# --- Base de datos del sistema ---
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_BD = os.path.join(DIRECTORIO_ACTUAL, "data", "base_datos.json")

sistema = {
    "empleados": {},
    "proyectos": {},
}

def cargar_datos():
    """lee el archivo JSON al iniciar el programa"""
    global sistema
    try:
        with open(ARCHIVO_BD, "r") as f:
            sistema = json.load(f)
    except FileNotFoundError:
        # Si no existe, iniciamos uno con la estructura vacía
        sistema = {"empleados": {}, "proyectos": {}}
def guardar_datos():
    """Sobreescribe el archivo JSON con los datos más recientes"""
    with open(ARCHIVO_BD, "w") as archivo:
        json.dump(sistema, archivo, indent=4)

# --- Funciones de Diseño UX---
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione Enter para continuar...")

def pedir_fecha(mensaje):
    while True:
        fecha_str = input (mensaje).strip()
        if not fecha_str:
            print("ERROR: La fecha no puede estar vacía. Por favor, ingrese una fecha válida.")
            continue

        try:
            # Validamos que la fecha esté en el formato correcto (DD/MM/AAAA)
            datetime.strptime(fecha_str, "%d/%m/%Y") 
            return fecha_str
        except ValueError:
            print("ERROR: Formato de fecha inválido. Por favor, ingrese la fecha en formato DD/MM/AAAA.")

# --- Modulo de registro de empleados ---
def registrar_empleado():
    print("\n--- REGISTRO DE NUEVO EMPLEADO ---")
    
    # Validamos que el ID no esté vacío 
    id_empleado = input("Ingrese el ID del empleado: ").strip().upper()
    while not id_empleado:
        print("ERROR: El ID del empleado no puede estar vacío. Por favor, ingrese un ID válido.")
        id_empleado = input("Ingrese el ID del empleado: ").strip().upper()

    # Validamos si el ID ya existe en el sistema
    if id_empleado in sistema["empleados"]:
        print("Error: El ID del empleado ya existe.")
    else:
        # Tambien validamos que el nombre no esté vacío
        nombre = input("Ingrese el nombre del empleado: ").strip()
        while not nombre:
            print("ERROR: El nombre del empleado no puede estar vacío. Por favor, ingrese un nombre válido.")
            nombre = input("Ingrese el nombre del empleado: ").strip()
        # Validamos que el cargo no esté vacío
        cargo = input("Ingrese el cargo del empleado: ").strip()
        while not cargo:
            print("ERROR: El cargo del empleado no puede estar vacío. Por favor, ingrese un cargo válido.")
            cargo = input("Ingrese el cargo del empleado: ").strip()

        # Agregamos al empleado al sistema
        sistema["empleados"][id_empleado] = {
            "nombre": nombre,
            "cargo": cargo,
            "registro_horas_diarias": {}
        }
        print(f"Empleado {nombre} registrado exitosamente con ID {id_empleado}.")

# --- Modulo de registro de proyectos ---
def registrar_proyecto():
    print("\n--- REGISTRO DE NUEVO PROYECTO ---")

    # Validamos que el ID del proyecto no esté vacío
    id_proyecto = input("Ingrese el ID del proyecto: ").strip().upper()
    while not id_proyecto:
        print("ERROR: El ID del proyecto no puede estar vacío. Por favor, ingrese un ID válido.")
        id_proyecto = input("Ingrese el ID del proyecto: ").strip().upper()
    
    if id_proyecto in sistema["proyectos"]:
        print("Error: Este Proyecto ya existe.")
    else: 
        # Validamos que el nombre del proyecto no esté vacío
        nombre_proyecto = input("Ingrese el nombre del proyecto: ").strip()
        while not nombre_proyecto:
            print("ERROR: El nombre del proyecto no puede estar vacío. Por favor, ingrese un nombre válido.")
            nombre_proyecto = input("Ingrese el nombre del proyecto: ").strip()

        fecha_inicio = pedir_fecha("Ingrese la fecha de inicio del proyecto (DD/MM/AAAA): ").strip()
        fecha_fin = pedir_fecha("Ingrese la fecha de fin del proyecto (DD/MM/AAAA): ").strip()

        # Agregamos el proyecto al sistema
        sistema["proyectos"][id_proyecto] = {
            "nombre": nombre_proyecto,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "tareas": [],
            "empleados_asignados": []
        }
        print(f"Proyecto {nombre_proyecto} registrado exitosamente con ID {id_proyecto}.")

# --- Modulo de registro de tareas ---
def registrar_tarea():
    print ("\n--- REGISTRO DE NUEVA TAREA ---")

    # Validamos si existen datos base antes de intentar relacionarlos
    if not sistema["proyectos"]:
        print("ERROR: No hay proyectos registrados. Por favor, registre un proyecto antes de agregar tareas.")
        return
    if not sistema["empleados"]:
        print("ERROR: No hay empleados registrados. Por favor, registre un empleado antes de agregar tareas.")
        return
    
    # 1. Selección del proyecto
    id_proyecto = input("Ingrese el ID del proyecto al que pertenece la tarea: ").strip().upper()
    while id_proyecto not in sistema["proyectos"]:
        print("ERROR: El ID del proyecto no existe. Por favor, ingrese un ID válido.")
        id_proyecto = input("Ingrese un ID de proyecto válido: ").strip().upper()

    # 2. Nombrar la tarea
    Nombre_tarea = input("Ingrese el nombre de la tarea: ").strip()
    while not Nombre_tarea:
        print("ERROR: El nombre de la tarea no puede estar vacío. Por favor, ingrese un nombre válido.")
        Nombre_tarea = input("Ingrese el nombre de la tarea: ").strip()
    
    # 3. Asignar un empleado a la tarea
    id_empleado = input("Ingrese el ID del empleado responsable: ").strip().upper()
    while id_empleado not in sistema["empleados"]:
        print("ERROR: El ID del empleado no existe. Por favor, ingrese un ID válido.")
        id_empleado = input("Ingrese un ID de empleado válido: ").strip().upper()

    # 4. Construir y guardar la tarea
    nueva_tarea = { 
        "nombre_tarea": Nombre_tarea,
        "empleado_asignado": id_empleado,
        "horas_invertidas": 0
    }
    sistema["proyectos"][id_proyecto]["tareas"].append(nueva_tarea)

    # 5. Agregar el empleado a la lista de empleados asignados al proyecto (si no está ya)
    if id_empleado not in sistema["proyectos"][id_proyecto]["empleados_asignados"]:
        sistema["proyectos"][id_proyecto]["empleados_asignados"].append(id_empleado)

    print(f"Tarea '{Nombre_tarea}' asignada exitosamente al empleado '{id_empleado}'.") 

# --- Modulo de registro de horas trabajadas ---
def registrar_horas():
    print("\n--- REGISTRO DE HORAS TRABAJADAS ---")

    if not sistema["proyectos"]:
        print("ERROR: No hay proyectos registrados. Por favor, registre un proyecto antes de registrar horas trabajadas.")
        return
    
    id_proyecto = input("Ingrese el ID del proyecto al que pertenece la tarea: ").strip().upper()
    if id_proyecto not in sistema["proyectos"]:
        print("ERROR: El ID del proyecto no existe. Por favor, ingrese un ID válido.")
        return
    
    proyecto = sistema["proyectos"][id_proyecto]
    if not proyecto["tareas"]:
        print("ERROR: No hay tareas registradas para este proyecto. Por favor, registre una tarea antes de registrar horas trabajadas.")
        return
    
    # Listamos las tareas del proyecto disponibles para seleccionar
    print("\nTareas disponibles para registrar horas trabajadas:")
    for i, tarea in enumerate(proyecto["tareas"]):
        print(f"{i + 1}. {tarea['nombre_tarea']} (Responsable: {tarea['empleado_asignado']})")
    
    # seleccionamos la tarea
    try:
        opcion_tarea = int(input("Seleccione el número de la tarea para registrar horas trabajadas: ").strip())
        if opcion_tarea < 1 or opcion_tarea > len(proyecto["tareas"]):
            print("ERROR: Opción de tarea inválida. Por favor, seleccione una opción válida.")
            return
    except ValueError:
        print("ERROR: Por favor, ingrese un número válido.")
        return
    
    tarea_seleccionada = proyecto["tareas"][opcion_tarea - 1]
    id_empleado = tarea_seleccionada["empleado_asignado"]

    # pedir la fecha de trabajo
    fecha_trabajo = pedir_fecha("Ingrese la fecha de trabajo (DD/MM/AAAA): ").strip()

    # pedir las horas trabajadas
    try:
        horas_nuevas = float(input("\nIngrese la cantidad de horas trabajadas: ").strip())
        if horas_nuevas <= 0:
            print("ERROR: La cantidad de horas trabajadas debe ser mayor a 0. Por favor, ingrese un valor válido.")
            return
    except ValueError:
        print("ERROR: Por favor, ingrese un número válido.")
        return
    # Validacion logica de 24 horas maximas por dia
    historial_empleado = sistema["empleados"][id_empleado]["registro_horas_diarias"]

    # Obtenemos las horas que ya trabajo ese día (si no ha trabajado ese día, asumimos 0 horas)
    horas_ya_registradas = historial_empleado.get(fecha_trabajo, 0)

    if horas_ya_registradas + horas_nuevas > 24:
        print(f"\n[!] ALERTA: Jornada irreal detectada.")
        print(f"El empleado {id_empleado} ya tiene {horas_ya_registradas} horas registradas para el día {fecha_trabajo}.")
        print(f"No puede añadir {horas_nuevas} horas más porque excedería el límite de 24 horas diarias.")
        return 
    # Si la validación es exitosa, registramos las horas
    historial_empleado[fecha_trabajo] = horas_ya_registradas + horas_nuevas 
    tarea_seleccionada["horas_invertidas"] += horas_nuevas

    print(f"\n¡Éxito! Se han registrado {horas_nuevas} horas a la tarea '{tarea_seleccionada['nombre_tarea']}' del proyecto '{proyecto['nombre']}'.")


# --- Modulo de Reporte de horas --- 
def generar_reportes():
    print("\n--- REPORTE DE HORAS POR PROYECTO ---")

    if not sistema["proyectos"]:
        print("ERROR: No hay proyectos registrados. Por favor, registre un proyecto antes de generar reportes.")
        return
    # Recorremos cada proyecto en el diccionario
    for id_proj, datos_proj in sistema["proyectos"].items():
        print(f"\n========================================")
        print(f"PROYECTO: {datos_proj['nombre']} (ID: {id_proj})")
        print(f"========================================")

        total_horas_proyecto = 0

        if not datos_proj["tareas"]:
            print("No hay tareas asignadas para este proyecto.")
        else:
            # Recorremos cada tarea del proyecto
            for tarea in datos_proj["tareas"]:
                horas_tarea = tarea["horas_invertidas"]
                total_horas_proyecto += horas_tarea
                print(f"  -> Tarea: {tarea['nombre_tarea']}")
                print(f"     Responsable: {tarea['empleado_asignado']}")
                print(f"     Horas invertidas: {horas_tarea}")
                print(f"  ----------------------------------------")
        
        print(f"TOTAL DE HORAS DE EL PROYECTO: {total_horas_proyecto}")
        print(f"========================================\n")

# --- Modulo de modificación de datos ---
def modificar_entidad():
    print("\n--- MENÚ DE MODIFICACIÓN ---")
    print("1. Modificar Empleado")
    print("2. Modificar Proyecto")
    print("3. Volver al menú principal")
    opc = input("Seleccione qué desea modificar: ").strip()

    if opc == "1":
        id_emp = input("Ingrese el ID del empleado a modificar (Enter para cancelar): ").strip().upper()
        if not id_emp:
            return
        while id_emp not in sistema["empleados"]:
            print("ERROR: Empleado no encontrado. Por favor, ingrese un ID válido.")
            id_emp = input("Ingrese un ID valido (Enter para cancelar): ").strip().upper()
            if not id_emp:
                return
        empleado = sistema["empleados"][id_emp]
        print(f"\nDatos actuales del empleado -> Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}")
        print("(Deje en blanco y presione Enter si no desea cambiar el dato)")

        nuevo_nombre = input("Nuevo nombre: ").strip()
        nuevo_cargo = input("Nuevo cargo: ").strip()
        
        if nuevo_nombre:
            empleado["nombre"] = nuevo_nombre
        if nuevo_cargo:
            empleado["cargo"] = nuevo_cargo

        print("\n¡Hecho! Los datos del empleado han sido actualizados.")

    elif opc == "2":
        id_proj = input("Ingrese el ID del proyecto a modificar (Enter para cancelar): ").strip().upper()
        if not id_proj:
            return  
        while id_proj not in sistema["proyectos"]:
            print("ERROR: Proyecto no encontrado. Por favor, ingrese un ID válido.")
            id_proj = input("Ingrese un ID valido (Enter para cancelar): ").strip().upper()
            if not id_proj:
                return
        
        proyecto = sistema["proyectos"][id_proj]
        print(f"\nDatos actuales del proyecto -> Nombre: {proyecto['nombre']} | Inicio: {proyecto['fecha_inicio']} | Fin: {proyecto['fecha_fin']}")
        print("(Deje en blanco y presione Enter si no desea cambiar el dato)")

        nuevo_nombre = input("Nuevo nombre del proyecto: ").strip()
        if nuevo_nombre:
            proyecto["nombre"] = nuevo_nombre

        print("\nPara las fechas:")
        cambiar_fechas = input("¿Desea cambiar las fechas del proyecto? (s/n): ").strip().lower()
        if cambiar_fechas == "s":
            nueva_fecha_inicio = pedir_fecha("Ingrese nueva fecha de inicio (DD/MM/AAAA): ").strip()
            nueva_fecha_fin = pedir_fecha("Ingrese nueva fecha de fin (DD/MM/AAAA): ").strip()
            
        print("\n¡Hecho! Los datos del proyecto han sido actualizados.")
        

# --- Modulo de Eliminación ---
def eliminar_entidad():
    print("\n--- MENÚ DE ELIMINACIÓN ---")
    print("1. Eliminar Empleado")
    print("2. Eliminar Proyecto")
    print("3. Volver al menú principal")
    opc = input("Seleccione qué desea eliminar: ")

    if opc == "1":
        id_emp = input("Ingrese el ID del empleado a eliminar: ").strip().upper()
        if not id_emp:
            return
        
        while id_emp not in sistema["empleados"]:
            print("ERROR: Empleado no encontrado. Por favor, ingrese un ID válido.")
            id_emp = input("Ingrese un ID valido (Enter para cancelar): ").strip().upper()
            if not id_emp:
                return
            
        if id_emp in sistema["empleados"]:
            nombre = sistema["empleados"][id_emp]["nombre"]
            del sistema["empleados"][id_emp]

            # Lo eliminamos de los proyectos donde estaba asignado
            for id_proj in sistema ["proyectos"]:
                # Lo removemos de la lista de personas asignadas
                if id_emp in sistema ["proyectos"][id_proj]["empleados_asignados"]:
                    sistema["proyectos"][id_proj]["empleados_asignados"].remove(id_emp) 
                
                # Actualizamos las tareas que tenian al empleado a eliminar
                for tarea in sistema["proyectos"][id_proj]["tareas"]:
                    if tarea["empleado_asignado"] == id_emp:
                        tarea["empleado_asignado"] = "SIN ASIGNAR"
            
            print(f"Empleado '{nombre}' eliminado y tareas actualizadas.")
        else:
            print("ERROR: Empleado no encontrado.")
    elif opc == "2":
        id_proj = input("Ingrese el ID del proyecto a eliminar: ").strip().upper()
        if not id_proj:
            return
        
        while id_proj not in sistema["proyectos"]:
            print("ERROR: Proyecto no encontrado. Por favor, ingrese un ID válido.")
            id_proj = input("Ingrese un ID valido (Enter para cancelar): ").strip().upper()
            if not id_proj:
                return
            
        if id_proj in sistema["proyectos"]:
            nombre = sistema ["proyectos"][id_proj]["nombre"]
            del sistema["proyectos"][id_proj]
            print(f"Proyecto '{nombre}' eliminado.")

# --- Prueba del sistema ---
if __name__ == "__main__":
    cargar_datos() # Leemos el archivo JSOn al abrir

    while True:
        limpiar_pantalla()
        print("========================================")
        print("      --- GESTOR DE PROYECTOS ---")
        print("========================================")
        print("1. Registrar nuevo empleado")
        print("2. Registrar nuevo proyecto")
        print("3. Registrar nueva tarea")
        print("4. Registrar horas trabajadas")
        print("5. Generar reporte de proyectos y horas")
        print("6. Modificar datos de empleado o proyecto")
        print("7. Eliminar empleado o proyecto")
        print("8. Salir")
        print("========================================")
        opcion = input("Seleccione una opción: ").strip()

        limpiar_pantalla() # Limpiamos antes de entrar al módulo

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            registrar_proyecto()
        elif opcion == "3":
            registrar_tarea()
        elif opcion == "4":
            registrar_horas()
        elif opcion == "5":
            generar_reportes()
        elif opcion == "6":
            modificar_entidad()
        elif opcion == "7":
            eliminar_entidad()
        elif opcion == "8":
            print ("Saliendo del sistema. ¡Hasta luego!")
            guardar_datos()
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        guardar_datos() # Guardamos los datos automáticamente en el JSON

        if opcion != "8":
            pausar() # pausamos para que el usuario lea lo que pasó1