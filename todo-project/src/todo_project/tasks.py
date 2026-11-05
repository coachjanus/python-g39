
from .model import Task


class TaskList:
    """A class representing a list of tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a new task to the list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list:
        """Return the list of tasks."""
        return self.tasks