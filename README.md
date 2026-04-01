# 🧪 Devin AI Test Project: Laboratorio de Ingeniería Autónoma

Bienvenido al proyecto de prueba para Devin AI (2026). Este es un entorno diseñado para que pruebes las **capacidades autónomas de Devin** en un escenario de desarrollo real, auditoría de seguridad y automatización de procesos.

## 📌 Estado Actual del Proyecto (Punto de Partida)
Este proyecto es una API básica de gestión de tareas con FastAPI:

1.  **Vulnerabilidades Críticas**: El archivo `requirements.txt` tiene versiones obsoletas (ej: `requests==2.28.1` y `fastapi==0.95.0`) con fallos de seguridad conocidos.
2.  **Falta de Calidad**: El archivo `main.py` contiene lógica de negocio pero **no tiene suite de tests unitarios**.
3.  **Holes en la Documentación**: No hay instrucciones de despliegue ni reporte de seguridad.

---

## 🎯 ¿Qué se espera que haga Devin?
Al ejecutar a Devin con el archivo `devin-init.yaml`, el agente debe trabajar de forma 100% autónoma en su VM para:

1.  **Escanear**: Descubrir las versiones vulnerables en el `requirements.txt` usando herramientas como `safety`.
2.  **Remediar**: Actualizar las dependencias a versiones seguras y estables de 2026 sin romper el código.
3.  **Automatizar**: Analizar el código de `main.py` y crear una carpeta `tests/` con la suite completa de `pytest`.
4.  **Validar (QA)**: Correr los tests y confirmar que todo funciona correctamente después del parche de seguridad.
5.  **Entregar**: Generar un reporte final de cambios.

---

## 🚀 Preparación y Ejecución (Local)

Para probar este código manualmente en tu notebook antes de entregárselo a Devin:

1.  **Crear el entorno virtual**:
    ```bash
    python -m venv venv
    ```
2.  **Activar el entorno**:
    *   En macOS/Linux: `source venv/bin/activate`
    *   En Windows: `venv\Scripts\activate`
3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ejecutar la API**:
    ```bash
    python main.py
    ```

---

## 🔑 Gestión de Credenciales y Secretos

### ¿Cómo se autentica Devin?
Devin NO necesita que le pases tus credenciales en un archivo `.env` para esta prueba básica. Devin utiliza tu sesión de la **`devin-cli`** o tu cuenta vinculada en **`app.devin.ai`** para obtener permisos de lectura/escritura en tus repositorios de GitHub.

### ¿Cuándo usar un .env?
Si tu proyecto real necesitara conectarse a una API externa (ej: una base de datos remota o una API de clima), deberías:
1. Crear un archivo `.env.example` con las claves vacías.
2. Pasar los secretos a Devin de forma segura a través de la interfaz de la plataforma o configurando las variables de entorno en su VM aislada.

---

## 🤖 Lanzar la Misión de Devin

Una vez suscrito y con la CLI instalada, lanza el experimento desde la raíz de este directorio:

```bash
devin run --file devin-init.yaml
```

**¡Observa la consola!** Verás a Devin tomar el control, planificar las tareas y "desaparecer" a trabajar en su VM propia (una infraestructura totalmente separada de tu notebook). Él mismo se encargará de instalar su propio entorno y dependencias. 🧠⚡
