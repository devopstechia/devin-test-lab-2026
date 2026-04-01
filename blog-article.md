# Cómo un agente de IA detectó y corrigió 16 vulnerabilidades de seguridad en una API de Python — en una sola sesión

Un recorrido real por la auditoría de seguridad autónoma, la remediación de dependencias y la automatización de pruebas en un proyecto FastAPI.

---

## El punto de partida: Una bomba de tiempo tecnológica

Imagina heredar un proyecto de API en Python. Funciona. Los endpoints responden. Los usuarios están contentos. Pero bajo la superficie, el archivo `requirements.txt` es un campo de minas:

```text
fastapi==0.95.0
uvicorn==0.21.0
pydantic==1.10.7
requests==2.28.1
safety==2.3.5
pytest==7.2.2
httpx==0.23.3
```

Cada uno de estos paquetes está desactualizado. Varios contienen CVEs (vulnerabilidades comunes) conocidos que los atacantes pueden explotar. Y no hay ni una sola prueba para detectar regresiones si intentas arreglarlos.

Esta es la historia de cómo un agente de IA autónomo (Devin) escaneó, parcheó, probó y entregó un pull request limpio —de principio a fin— sin romper ni una sola línea del código de la aplicación.

---

## Paso 1: Entendiendo el código base

El proyecto es una **API gestora de tareas con FastAPI** — simple pero representativa de los microservicios del mundo real. Tiene tres endpoints básicos:

```python
@app.get("/tasks")           # Listar todas las tareas
@app.post("/tasks")          # Crear una nueva tarea
@app.get("/tasks/{task_id}") # Obtener una tarea por ID (o 404)
```

Las tareas se almacenan en una lista en memoria y se usa un modelo Pydantic para la validación. Eso es todo —unas 40 líneas de código—. La simplicidad es engañosa, porque el peligro real vive en las dependencias.

---

## Paso 2: Escaneo de vulnerabilidades

El primer paso fue instalar las dependencias actuales y ejecutar `pip-audit`, un escáner de vulnerabilidades mantenido por el Python Packaging Authority (PyPA):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pip-audit
pip-audit -r requirements.txt
```

El resultado fue alarmante:

```text
Se encontraron 16 vulnerabilidades conocidas en 6 paquetes
```

### Desglose de los hallazgos

Aquí están los problemas más críticos detectados por Devin:

#### Denegación de Servicio (DoS)
- **FastAPI 0.95.0** (PYSEC-2024-38): Un atacante podría bloquear el servidor enviando datos de formularios multipart malformados. Esto es peligroso porque no requiere autenticación —basta con una petición HTTP maliciosa—.
- **Starlette 0.26.1** (PYSEC-2023-83): El framework ASGI que sustenta FastAPI era vulnerable al agotamiento de memoria mediante cargas de archivos. Un atacante podía consumir toda la RAM disponible con una sola petición.

#### HTTP Request Smuggling (Contrabando de Peticiones)
- **h11 0.14.0** (CVE-2025-43859): El manejo incorrecto de las cabeceras `Content-Length` permitía "colar" peticiones a través de proxies de seguridad, accediendo potencialmente a endpoints restringidos.
- **urllib3 1.26.20** (CVE-2026-21441): Contrabando similar mediante cabeceras `Transfer-Encoding` malformadas.

#### Filtrado de Información y SSRF
- **requests 2.28.1** (PYSEC-2023-74): La cabecera `Proxy-Authorization` se filtraba al seguir redirecciones a hosts diferentes.
- **requests 2.28.1** (CVE-2024-47081): Server-Side Request Forgery mediante URIs `file://` — un atacante podría leer archivos del sistema del servidor—.

#### Bypass de Verificación de Certificados
- **requests 2.28.1** (CVE-2024-35195): Después de llamar a `verify=False` en una petición, las siguientes peticiones en la misma `Session` omitían silenciosamente la verificación de certificados.

### Resumen de Severidad

| Severidad | Cantidad | Ejemplos |
| :--- | :--- | :--- |
| **Alta** | 7 | Request smuggling, DoS, SSRF |
| **Media** | 9 | Fuga de credenciales, ReDoS |

Siete de las dieciséis vulnerabilidades fueron calificadas como **Severidad Alta**, lo que significa que podían explotarse remotamente con mínimo esfuerzo e impacto significativo.

---

## Paso 3: El desafío de la remediación

Actualizar dependencias no es solo subir números de versión. Es un rompecabezas de compatibilidad:

### El Problema Pydantic v1 vs v2
Pydantic 2.0 fue una **reescritura total**. Cambió el comportamiento de validación y las APIs internas. Devin tuvo que verificar si nuestra app de 40 líneas sobreviviría al cambio. El diagnóstico: la app solo usaba funciones básicas de `BaseModel` compatibles con la nueva versión.

### La cadena de versiones de Starlette
FastAPI fija su dependencia de Starlette. Para obtener un Starlette totalmente parcheado (1.0.0), Devin tuvo que saltar hasta FastAPI 0.135.3, la última versión estable.

### Mapa Final de Dependencias

| Paquete | Antes | Después | Salto |
| :--- | :--- | :--- | :--- |
| **fastapi** | 0.95.0 | 0.135.3 | 40 versiones menores |
| **uvicorn** | 0.21.0 | 0.34.2 | 13 versiones menores |
| **pydantic** | 1.10.7 | 2.12.5 | Versión Mayor (v1 a v2) |
| **requests** | 2.28.1 | 2.33.1 | 5 versiones menores |
| **starlette** | 0.26.1 | 1.0.0 | Versión Mayor (transitiva) |

**Resultado final del escaneo tras la actualización:**
```bash
$ pip-audit
No se encontraron vulnerabilidades conocidas
```

---

## Paso 4: Construyendo la red de seguridad (Suite de Tests)

Sin pruebas existentes, la actualización era un acto de fe. Devin diseñó una suite de **11 tests con Pytest** bajo estos principios:
1.  **Cubrir todos los endpoints**: Listado, creación y obtención por ID.
2.  **Probar caminos felices y de error**: Validó respuestas 200, 400 (duplicados), 404 (no encontrado) y 422 (validación fallida).
3.  **Aislamiento**: Cada test comienza con una base de datos limpia.

```text
============================== 11 pasados en 0.55s ==============================
```

---

## Paso 5: Verificación End-to-End en la VM

Las pruebas unitarias son geniales, pero Devin fue un paso más allá. Levantó el servidor real en su VM y atacó los endpoints manualmente con `curl`:

```bash
# 1. Lista vacía
$ curl -s http://localhost:8000/tasks
[]

# 2. Crear una tarea
$ curl -s -X POST http://localhost:8000/tasks -d '{"id": 1, "title": "Test Devin"}'
{"id":1,"title":"Test Devin",...}
```

Además, probó la API a través de la **Swagger UI** integrada (`/docs`), capturando una grabación de pantalla como evidencia visual del éxito.

---

## Impacto Final

| Métrica | Antes | Después |
| :--- | :--- | :--- |
| Vulnerabilidades conocidas | **16** | **0** |
| Cobertura de tests | **0 tests** | **11 tests** |
| Código de aplicación modificado | — | **0 líneas** |
| Paquetes actualizados | — | **9 paquetes** |

**La gran lección**: El número más importante no es 16 ni 0. Es **0 líneas de código de aplicación modificadas**. Toda la remediación se logró mediante actualizaciones inteligentes de dependencias, demostrando que estar al día es la defensa más efectiva.

---

*Esta auditoría fue realizada de forma autónoma por Devin AI el 1 de abril de 2026. Todo el proceso —desde el clonado hasta el Pull Request final— se completó en una sola sesión.*
