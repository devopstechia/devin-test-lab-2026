import pytest
from fastapi.testclient import TestClient

from main import app, tasks_db


@pytest.fixture(autouse=True)
def clear_tasks_db():
    """Clear the in-memory database before each test."""
    tasks_db.clear()
    yield
    tasks_db.clear()


class TestGetTasks:
    """Tests for GET /tasks endpoint."""

    def test_get_tasks_empty(self):
        """Should return an empty list when no tasks exist."""
        client = TestClient(app)
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_tasks_with_data(self):
        """Should return all tasks after creating some."""
        client = TestClient(app)
        task_data = {"id": 1, "title": "Test Task", "description": "A test", "completed": False}
        client.post("/tasks", json=task_data)

        response = client.get("/tasks")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) == 1
        assert tasks[0]["title"] == "Test Task"

    def test_get_tasks_multiple(self):
        """Should return multiple tasks."""
        client = TestClient(app)
        client.post("/tasks", json={"id": 1, "title": "Task 1"})
        client.post("/tasks", json={"id": 2, "title": "Task 2"})
        client.post("/tasks", json={"id": 3, "title": "Task 3"})

        response = client.get("/tasks")
        assert response.status_code == 200
        assert len(response.json()) == 3


class TestCreateTask:
    """Tests for POST /tasks endpoint."""

    def test_create_task_minimal(self):
        """Should create a task with only required fields."""
        client = TestClient(app)
        task_data = {"id": 1, "title": "Minimal Task"}
        response = client.post("/tasks", json=task_data)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["title"] == "Minimal Task"
        assert data["description"] is None
        assert data["completed"] is False

    def test_create_task_full(self):
        """Should create a task with all fields provided."""
        client = TestClient(app)
        task_data = {
            "id": 10,
            "title": "Full Task",
            "description": "A complete task",
            "completed": True,
        }
        response = client.post("/tasks", json=task_data)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 10
        assert data["title"] == "Full Task"
        assert data["description"] == "A complete task"
        assert data["completed"] is True

    def test_create_task_duplicate_id(self):
        """Should return 400 when creating a task with a duplicate ID."""
        client = TestClient(app)
        task_data = {"id": 1, "title": "First Task"}
        client.post("/tasks", json=task_data)

        duplicate = {"id": 1, "title": "Duplicate Task"}
        response = client.post("/tasks", json=duplicate)
        assert response.status_code == 400
        assert response.json()["detail"] == "El ID ya existe."

    def test_create_task_missing_title(self):
        """Should return 422 when title is missing."""
        client = TestClient(app)
        response = client.post("/tasks", json={"id": 1})
        assert response.status_code == 422

    def test_create_task_missing_id(self):
        """Should return 422 when id is missing."""
        client = TestClient(app)
        response = client.post("/tasks", json={"title": "No ID"})
        assert response.status_code == 422


class TestGetTaskById:
    """Tests for GET /tasks/{task_id} endpoint."""

    def test_get_task_by_id(self):
        """Should return the correct task by ID."""
        client = TestClient(app)
        task_data = {"id": 5, "title": "Find Me", "description": "Searchable"}
        client.post("/tasks", json=task_data)

        response = client.get("/tasks/5")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 5
        assert data["title"] == "Find Me"
        assert data["description"] == "Searchable"

    def test_get_task_not_found(self):
        """Should return 404 when task ID does not exist."""
        client = TestClient(app)
        response = client.get("/tasks/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Tarea no encontrada."

    def test_get_task_among_many(self):
        """Should return the correct task when multiple tasks exist."""
        client = TestClient(app)
        client.post("/tasks", json={"id": 1, "title": "Task A"})
        client.post("/tasks", json={"id": 2, "title": "Task B"})
        client.post("/tasks", json={"id": 3, "title": "Task C"})

        response = client.get("/tasks/2")
        assert response.status_code == 200
        assert response.json()["title"] == "Task B"
