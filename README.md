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

## 🚀 Instrucciones de Ejecución (Notebook Local)

1.  Asegúrate de tener instalada la `devin-cli`.
2.  Asegúrate de estar suscrito al plan Core o Team de Devin.
3.  Desde la raíz de este directorio (`devin_test_project`), ejecuta:

```bash
devin run --file devin-init.yaml
```

**¡Observa la consola!** Verás a Devin tomar el control, planificar las tareas y "desaparecer" a trabajar en su VM. Vuelve cuando el proyecto esté seguro y testeado. 🧠⚡
