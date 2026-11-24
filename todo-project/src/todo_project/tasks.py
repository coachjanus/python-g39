
from pathlib import Path
from typing import Dict, List
from .model import Task
from .priority import Priority
from .dbhandler import DBHandler
from .responses import TodoResponse
from .config import SUCCESS, ID_ERROR


class TaskList:
    """Manages tasks in memory using a dictionary for O(1) lookups."""

    def __init__(self, db_path: Path) -> None:
        self._db_handler = DBHandler(db_path)
        response = self._db_handler.load_from_file()
        self._tasks: Dict[int, Task] = {task.id: task for task in response.data}
        self._next_id = max(self._tasks.keys(), default=0) + 1

    def _save(self) -> int:
        return self._db_handler.save_to_file(list(self._tasks.values())).error

    def add_task(self, description: str, priority: Priority = Priority.NORMAL) -> TodoResponse:
        task = Task(id=self._next_id, description=description, priority=priority)
        self._tasks[task.id] = task
        self._next_id += 1
        error = self._save()
        return TodoResponse(task, error)

    def remove_task(self, task_id: int) -> TodoResponse | None:
        task = self._tasks.pop(task_id, None)
        if not task:
            return None
        error = self._save()
        return TodoResponse(task, error)

    def get_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def mark_completed(self, task_id: int) -> TodoResponse | None:
        task = self._tasks.get(task_id)
        if not task:
            return None
        task.mark_completed()
        error = self._save()
        return TodoResponse(task, error)

    def set_priority(self, task_id: int, priority: Priority) -> TodoResponse | None:
        task = self._tasks.get(task_id)
        if not task:
            return None
        task.priority = priority
        error = self._save()
        return TodoResponse(task, error)