Algoritmo Gestor_Proyectos
    Definir opc Como Entero
    Definir ejecucion Como Logico
    ejecucion <- Verdadero
    
    Mientras ejecucion Hacer
        Escribir ""
        Escribir "==========================================="
        Escribir "       SISTEMA DE GESTION DE PROYECTOS     "
        Escribir "==========================================="
        Escribir "1. Registro de Empleados y Proyectos"
        Escribir "2. Gestion de Tareas y Asignaciones"
        Escribir "3. Reporte de Horas y Validacion"
        Escribir "4. Salir del Sistema"
        Escribir "-------------------------------------------"
        Escribir "Seleccione una opcion (1-4):"
        Leer opc
        
        Segun opc Hacer
            1:
                RegistrarEntidades()
            2:
                AdministrarTareas()
            3:
                ProcesarHoras()
            4:
                Escribir "Finalizando programa..."
                ejecucion <- Falso
            De Otro Modo:
                Escribir "Opcion no valida."
        FinSegun
    FinMientras
FinAlgoritmo
//Opcion 1
SubProceso RegistrarEntidades
    Definir nEmp, nProy Como Cadena
    Escribir ""
    Escribir ">>> MODULO: REGISTRO DE DATOS"
    Escribir "Ingrese el nombre del empleado:"
    Leer nEmp
    Escribir "Ingrese el nombre del proyecto:"
    Leer nProy
    
    Escribir "-------------------------------------------"
    Escribir "EXITO: Empleado ", nEmp, " asignado a ", nProy
FinSubProceso
//Opcion 2
SubProceso AdministrarTareas
    Definir dTarea, resp Como Cadena
    Escribir ""
    Escribir ">>> MODULO: GESTION DE TAREAS"
    Escribir "Descripcion de la tarea:"
    Leer dTarea
    Escribir "Nombre del responsable:"
    Leer resp
    
    Escribir "-------------------------------------------"
    Escribir "CONFIRMACION: Tarea ", dTarea, " creada para ", resp
FinSubProceso
//Opcion 3
SubProceso ProcesarHoras
    Definir cHoras Como Real
    Escribir ""
    Escribir ">>> MODULO: CONTROL DE TIEMPOS"
    Escribir "Ingrese las horas trabajadas (0-24):"
    Leer cHoras
    // Logica de negocio: Validacion de jornada real
    Si cHoras > 0 Y cHoras <= 24 Entonces
        Escribir "-------------------------------------------"
        Escribir "REGISTRO VALIDO: Se han contabilizado ", cHoras, " horas."
    Sino
        Escribir "-------------------------------------------"
        Escribir "ALERTA: Jornada laboral irreal (Maximo 24h)."
    FinSi
FinSubProceso