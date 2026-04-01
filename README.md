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

## 🚀 Instrucciones de Ejecución (100% Web)

Para probar a Devin sin instalar nada en tu computadora, sigue estos pasos:

1.  **Haz un Fork de este repositorio**: Haz clic en el botón **"Fork"** en la esquina superior derecha para tener tu propia copia en tu cuenta de GitHub.
2.  **Inicia tu sesión en Devin**: Accede a **[app.devin.ai](https://app.devin.ai)** e inicia una **Nueva Sesión**.
3.  **Vincula tu copia**: Escribe a Devin: *"I want to work on my forked repository devin-test-lab-2026"*.
4.  **Lanza la Misión**: Una vez vinculado, dile: *"Read the `devin-init.yaml` file and execute all tasks defined there"*.

---

## 🖥️ ¿Qué sucederá en tu navegador? (La VM de Devin)

Al iniciar la sesión, verás cómo se abre una **Máquina Virtual (VM) dedicada** dentro del dashboard de Devin. No necesitas descargar nada porque Devin cuenta con su propio entorno de ejecución en la nube que incluye:
*   **Terminal de Linux**: Donde Devin instalará las dependencias y ejecutará los diagnósticos de seguridad.
*   **Editor de Código (IDE)**: Donde verás a Devin crear la carpeta de tests y editar los archivos en tiempo real.
*   **Navegador Web Interno**: Si Devin necesita consultar documentación técnica, verás cómo navega por internet dentro de la propia interfaz.

---

## 🛡️ Gestión de Seguridad y Permisos
Devin utiliza la conexión segura de tu cuenta de GitHub (vía OAuth) para clonar tu copia del repositorio y realizar los cambios (Commits y Pull Requests). No necesitas configurar archivos `.env` locales ni tokens manuales para esta prueba. Toda la infraestructura de ejecución vive y muere en la nube de Cognition AI. ⚡
