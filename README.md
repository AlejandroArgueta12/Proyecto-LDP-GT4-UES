# Gestor de Proyectos Simple - Ciclo 1/2026

## Descripción del Proyecto

Gestor de Proyectos Simple es una aplicación de escritorio desarrollada en Python que permite administrar empleados, proyectos y tareas dentro de una organización. El sistema incorpora una interfaz gráfica amigable, control de acceso basado en roles y mecanismos de validación que garantizan la integridad de la información almacenada.

La aplicación fue diseñada siguiendo principios de Programación Orientada a Objetos y una arquitectura modular que separa la lógica de negocio, la persistencia de datos y la interfaz gráfica de usuario.

---

## Integrantes

**Mauricio Alejandro Argueta Rodríguez**

**Fernando José Tesorero Brito**

---

## Objetivos del Sistema

* Gestionar empleados, proyectos y tareas de forma centralizada.
* Controlar las horas trabajadas por cada empleado.
* Garantizar la integridad de los datos mediante validaciones.
* Implementar control de acceso según el rol del usuario.
* Mantener la información almacenada de forma persistente utilizando archivos JSON.

---

## Características Principales

### Interfaz Gráfica de Usuario

* Navegación intuitiva mediante ventanas y formularios interactivos.
* Gestión de empleados, proyectos y tareas desde una interfaz visual.
* Visualización de reportes del sistema.
* Diseño modular y fácil de mantener.
* Implementada utilizando la librería Tkinter.

### Sistema de Roles

#### Administrador

* Registrar empleados.
* Gestionar empleados existentes.
* Registrar proyectos.
* Gestionar proyectos existentes.
* Crear tareas.
* Asignar tareas a proyectos.
* Asignar tareas a trabajadores.
* Consultar reportes de empleados, proyectos y tareas.
* Eliminar y actualizar registros.

#### Trabajador

* Consultar tareas asignadas.
* Registrar horas trabajadas.
* Consultar información relacionada con su trabajo.

---

## Arquitectura del Sistema

El proyecto está dividido en tres capas principales:

### Interfaz Gráfica

Responsable de la interacción con el usuario mediante ventanas, formularios y controles gráficos desarrollados con Tkinter.

### Lógica de Negocio

Implementada en el módulo `controlador_datos.py`, donde se encuentran las validaciones, reglas de negocio y operaciones principales del sistema.

### Persistencia de Datos

Responsable de almacenar y recuperar información utilizando archivos JSON, permitiendo conservar los datos entre ejecuciones.

---

## Características Implementadas

### Gestión de Empleados

* Registro de trabajadores.
* Consulta de información.
* Actualización de datos.
* Eliminación de registros.

### Gestión de Proyectos

* Registro de proyectos.
* Consulta de proyectos.
* Actualización de información.
* Eliminación de proyectos.

### Gestión de Tareas

* Registro de tareas.
* Asignación de tareas a proyectos.
* Asignación de tareas a trabajadores.
* Control de horas invertidas.

---

## Validaciones y Reglas de Negocio

El sistema implementa diversas validaciones para garantizar la consistencia de la información:

* Prevención de registros con identificadores duplicados.
* Verificación de existencia de empleados, proyectos y tareas.
* Restricción de jornadas laborales superiores a 24 horas por día.
* Validación de horas mayores a cero.
* Validación de datos numéricos para el registro de horas.
* Control de tareas asignadas antes de registrar horas.
* Manejo estructurado de excepciones para evitar errores inesperados.

---

## Persistencia de Datos

* Almacenamiento permanente mediante archivos JSON.
* Lectura y escritura centralizada desde el controlador de datos.
* Separación entre interfaz gráfica, lógica de negocio y almacenamiento.
* Recuperación automática de información al iniciar el sistema.

---

## Pruebas Unitarias

El sistema incluye pruebas automatizadas desarrolladas utilizando la librería estándar `unittest` de Python.

### Casos de prueba implementados

#### 1. Validación de jornada máxima

Verifica que un empleado no pueda registrar más de 24 horas de trabajo durante un mismo día.

#### 2. Integridad de identificadores duplicados

Comprueba que el sistema impida registrar empleados con un ID ya existente.

#### 3. Registro de horas en tareas inexistentes

Verifica que no sea posible registrar horas sobre tareas que no existen en el sistema.

#### 4. Registro válido de horas

Comprueba que el sistema permita registrar correctamente una cantidad válida de horas.

#### 5. Validación de horas negativas

Verifica que el sistema rechace cantidades de horas menores o iguales a cero.

#### 6. Validación de valores no numéricos

Comprueba que el sistema rechace entradas que no correspondan a valores numéricos.

### Ejecución de pruebas

Para ejecutar las pruebas unitarias:

```bash
python test_sistema.py
```

Resultado esperado:

```text
......
----------------------------------------------------------------------
Ran 6 tests

OK
```

---

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Acceder al directorio del proyecto

```bash
cd Proyecto-LDP-GT4-UES
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

---

## Tecnologías Utilizadas

* Python
* Tkinter
* JSON
* Programación Orientada a Objetos (POO)
* unittest
* Git
* GitHub

---

## Estado del Proyecto

Proyecto académico desarrollado para el ciclo 1/2026 como parte de la asignatura de Lenguajes de Programación, aplicando conceptos de Programación Orientada a Objetos, interfaces gráficas, persistencia de datos y pruebas unitarias.
