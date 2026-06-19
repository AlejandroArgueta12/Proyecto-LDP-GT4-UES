# Gestor de Proyectos Simple - Ciclo 1/2026

## Descripción del Proyecto
Este proyecto consiste en una aplicación de escritorio con interfaz gráfica que permite gestionar empleados, proyectos y tareas, además de registrar las horas trabajadas por cada empleado. El sistema incorpora control de acceso mediante roles, diferenciando entre administradores y trabajadores, así como validaciones para garantizar la integridad de la información almacenada.

## Integrantes
**Mauricio Alejandro Argueta Rodriguez**

**Fernando José Tesorero Brito**

## Características Principales
## Interfaz Gráfica de Usuario
* Navegación intuitiva mediante ventanas y formularios interactivos.
* Diseño modular para la gestión de empleados, proyectos, tareas y reportes.
* Implementada utilizando la librería Tkinter.

## Sistema de Roles
**Administrador**
* Crear y gestionar empleados.
* Crear y gestionar proyectos.
* Crear tareas.
* Asignar tareas a proyectos.
* Asignar tareas a trabajadores.
* Consultar reportes e información general del sistema.

**Trabajador**
* Registrar horas trabajadas.
* Consultar información relacionada con sus tareas asignadas.

## Características Implementadas
### Validaciones y Reglas de Negocio
* Prevención de registros con identificadores duplicados.
* Validación de formatos de fecha.
* Restricción de jornadas superiores a 24 horas por día por empleado.
* Manejo estructurado de excepciones para evitar fallos inesperados.

### Persistencia de Datos
* Almacenamiento permanente mediante archivos JSON.
* Lectura y escritura centralizada desde el controlador de datos.
* Identificación clara de separación entre la interfaz visual y el almacenamiento.

### Pruebas Unitarias
* Implementación de pruebas automatizadas utilizando la librería nativa "unittest".
* Verificación de las reglas de negocio y validaciones principales de forma aislada.

## Instalación y ejecución
**1. Clonar el repositorio:**
git clone "url-del-repositorio"

**2. Acceder al directorio del proyecto:**
cd "proyecto final"

**3. Instalar dependencias:**
pip install -r requirements.txt

**4. Ingresar a la carpeta principal de la aplicación:**
cd python

**5. Ejecutar el sistema:**
python app.py

## Tecnologías Utilizadas
* Python
* Tkinter
* JSON
* Programación Orientadas a Objetos
* unittest
* Git y Github
