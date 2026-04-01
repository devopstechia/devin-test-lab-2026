from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Devin Test Task Manager")

# Esquema para las tareas
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Simulación de base de datos en memoria
tasks_db: List[Task] = []

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """Retorna todas las tareas."""
    return tasks_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """Crea una nueva tarea."""
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="El ID ya existe.")
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Busca una tarea por su ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
