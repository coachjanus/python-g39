
from todo_project.priority import Priority


class Task:
    """Represents a task in the todo application."""

    def __init__(self, id: int, description: str = "", priority: Priority = Priority.NORMAL, completed: bool = False):
        self.id = id
        # self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] : {self.description}"
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
        id=data["id"],
        description=data["description"],
        completed=data.get("completed", False),
        priority=Priority(data.get("priority", 0)),
        )
        
    def to_dict(self):
        return {
        "id": self.id,
        "description": self.description,
        "completed": self.completed,
        "priority": self.priority,
        }