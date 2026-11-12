
import json
import os
from typing import List

from .model import Task
from pathlib import Path

class TaskList:
    """A class representing a list of tasks."""

    def __init__(self, db_path:Path):
        self.db_path = db_path
        self.tasks: List[Task] = []
        self.load_from_file()

    def add_task(self, description: str, priority: str = "normal") -> None:
        """Add a new task to the list."""
        task = Task(id=len(self.tasks) + 1, description=description, priority=priority)
        self.tasks.append(task)
        self.save_to_file()
        return task

    def remove_task(self, task: Task) -> None:
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list:
        """Return the list of tasks."""
        return self.tasks
    
    def mark_completed(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def set_priority(self, task_id: int, priority: str):
        for task in self.tasks:
            if task.id == task_id:
                task.priority = priority
                return True
        return False
    
    def save_to_file(self):
        with open(self.db_path, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
            
    def load_from_file(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(item) for item in data]
            except (json.JSONDecodeError, ValueError):
                self.tasks = []