# Devin AI Test Project: Laboratorio de Ingenieria Autonoma

API basica de gestion de tareas con FastAPI.

## Estado del Proyecto

Este proyecto es una API REST para gestion de tareas (CRUD) construida con FastAPI. Incluye:

- **Endpoints**: `GET /tasks`, `POST /tasks`, `GET /tasks/{task_id}`
- **Suite de tests**: 11 tests con pytest cubriendo todos los endpoints
- **Dependencias seguras**: Todas las dependencias actualizadas sin vulnerabilidades conocidas

---

## Reporte de Auditoria de Seguridad

### Vulnerabilidades Encontradas (16 en 6 paquetes)

| Paquete    | Version Anterior | CVEs / IDs                                                        | Version Segura |
|------------|------------------|-------------------------------------------------------------------|----------------|
| fastapi    | 0.95.0           | PYSEC-2024-38                                                     | 0.135.3        |
| pydantic   | 1.10.7           | CVE-2024-3772                                                     | 2.12.5         |
| requests   | 2.28.1           | PYSEC-2023-74, CVE-2024-35195, CVE-2024-47081, CVE-2026-25645     | 2.33.1         |
| httpx      | 0.23.3           | (outdated, transitive vulnerabilities)                             | 0.28.1         |
| starlette  | 0.26.1           | PYSEC-2023-83, CVE-2024-47874, CVE-2025-54121                     | 1.0.0          |
| urllib3    | 1.26.20          | CVE-2025-50181, CVE-2025-66418, CVE-2025-66471, CVE-2026-21441    | 2.6.3          |
| h11        | 0.14.0           | CVE-2025-43859                                                     | 0.16.0         |

### Acciones Realizadas

1. **Escaneo**: Se utilizo `pip-audit` para identificar 16 vulnerabilidades criticas en las dependencias.
2. **Remediacion**: Se actualizaron todas las dependencias a versiones seguras y estables:
   - `fastapi`: 0.95.0 -> 0.135.3
   - `uvicorn`: 0.21.0 -> 0.34.2
   - `pydantic`: 1.10.7 -> 2.12.5
   - `requests`: 2.28.1 -> 2.33.1
   - `pytest`: 7.2.2 -> 8.4.2
   - `httpx`: 0.23.3 -> 0.28.1
   - Se elimino `safety==2.3.5` (obsoleto, reemplazado por `pip-audit`)
3. **Automatizacion**: Se creo la carpeta `tests/` con una suite de 11 tests usando pytest.
4. **Validacion (QA)**: Se ejecuto pytest y se confirmo que los 11 tests pasan correctamente con las dependencias actualizadas.

### Resultado Final

```
pip-audit: No known vulnerabilities found
pytest: 11 passed
```

---

## Instrucciones de Ejecucion

### Ejecucion Local

1. **Crear el entorno virtual**:
    ```bash
    python -m venv venv
    ```
2. **Activar el entorno**:
    - En macOS/Linux: `source venv/bin/activate`
    - En Windows: `venv\Scripts\activate`
3. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Ejecutar la API**:
    ```bash
    python main.py
    ```
5. **Ejecutar los tests**:
    ```bash
    pytest tests/ -v
    ```

### Ejecucion 100% Web (con Devin)

Para probar a Devin sin instalar nada en tu computadora, sigue estos pasos:

1.  **Haz un Fork de este repositorio**: Haz clic en el boton **"Fork"** en la esquina superior derecha para tener tu propia copia en tu cuenta de GitHub.
2.  **Inicia tu sesion en Devin**: Accede a **[app.devin.ai](https://app.devin.ai)** e inicia una **Nueva Sesion**.
3.  **Vincula tu copia**: Escribe a Devin: *"I want to work on my forked repository devin-test-lab-2026"*.
4.  **Lanza la Mision**: Una vez vinculado, dile: *"Read the `devin-init.yaml` file and execute all tasks defined there"*.

---

## Suite de Tests

La suite cubre los siguientes escenarios:

| Test                              | Endpoint              | Descripcion                                     |
|-----------------------------------|-----------------------|-------------------------------------------------|
| test_get_tasks_empty              | GET /tasks            | Lista vacia cuando no hay tareas                |
| test_get_tasks_with_data          | GET /tasks            | Lista con una tarea creada                      |
| test_get_tasks_multiple           | GET /tasks            | Lista con multiples tareas                      |
| test_create_task_minimal          | POST /tasks           | Crear tarea con campos minimos                  |
| test_create_task_full             | POST /tasks           | Crear tarea con todos los campos                |
| test_create_task_duplicate_id     | POST /tasks           | Error 400 al duplicar ID                        |
| test_create_task_missing_title    | POST /tasks           | Error 422 sin titulo                            |
| test_create_task_missing_id       | POST /tasks           | Error 422 sin ID                                |
| test_get_task_by_id               | GET /tasks/{task_id}  | Obtener tarea existente por ID                  |
| test_get_task_not_found           | GET /tasks/{task_id}  | Error 404 tarea no encontrada                   |
| test_get_task_among_many          | GET /tasks/{task_id}  | Obtener tarea correcta entre varias             |

---

## La VM de Devin

Al iniciar la sesion, veras como se abre una **Maquina Virtual (VM) dedicada** dentro del dashboard de Devin. No necesitas descargar nada porque Devin cuenta con su propio entorno de ejecucion en la nube que incluye:
*   **Terminal de Linux**: Donde Devin instalara las dependencias y ejecutara los diagnosticos de seguridad.
*   **Editor de Codigo (IDE)**: Donde veras a Devin crear la carpeta de tests y editar los archivos en tiempo real.
*   **Navegador Web Interno**: Si Devin necesita consultar documentacion tecnica, veras como navega por internet dentro de la propia interfaz.

---

## Gestion de Seguridad y Permisos
Devin utiliza la conexion segura de tu cuenta de GitHub (via OAuth) para clonar tu copia del repositorio y realizar los cambios (Commits y Pull Requests). No necesitas configurar archivos `.env` locales ni tokens manuales para esta prueba.
