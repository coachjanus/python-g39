"""Represents a task in the todo application."""
 
from dataclasses import dataclass, asdict
from todo_project.priority import Priority
# Використання @dataclass для моделі Task (model.py): 
# Замість ручного написання __init__ та to_dict(), використайте стандартний @dataclass з dataclasses.asdict. 
# Це зменшить кількість коду вдвічі і зробить його чистішим.
@dataclass
class Task:
    id: int
    description: str = ""
    priority: Priority = Priority.NORMAL
    completed: bool = False

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] : {self.description}"

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data["id"],
            description=data["description"],
            completed=data.get("completed", False),
            priority=Priority(data.get("priority", 0)),
        )

    def to_dict(self) -> dict:
        return asdict(self)