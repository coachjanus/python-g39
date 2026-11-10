
from todo_project.priority import Priority


class Task:
    """Represents a task in the todo application."""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = Priority.NORMAL

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"