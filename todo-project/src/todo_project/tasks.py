
# import json
# import os
# from typing import List

from .model import Task
from pathlib import Path
from .dbhandler import DBHandler
from typing import Dict, List
from .responses import TodoResponse
from .config import SUCCESS

class TaskList:
    """A class representing a list of tasks."""

    def __init__(self, db_path:Path)->None:
        self._db_handler = DBHandler(db_path)
        response = self._db_handler.load_from_file()
        self._tasks: List[Task] = [task for task in response.data]
        # print(self._tasks)
        # self._tasks: Dict[int, Task] = {task.id: task for task in response.data}
        self._next_id = 1 if not self._tasks else len(self._tasks) + 1


    def add_task(self, description: str, priority: str = "normal") -> TodoResponse:
        """Add a new task to the list."""
        task_id = self._next_id
        task = Task(task_id, description=description, priority=priority)
        # self._tasks[task_id] = task
        self._tasks.append(task)
        self._next_id += 1
        # print(self._tasks[task_id])
        # self.tasks.append(task)
        # self.save_to_file()
        # return task
        response = self._db_handler.save_to_file(self._tasks)
        if response.error == SUCCESS:
            return TodoResponse(task, response.error)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list:
        """Return the list of tasks."""
        return self._tasks
    
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
    
    # def save_to_file(self):
    #     with open(self.db_path, 'w') as f:
    #         json.dump([task.to_dict() for task in self.tasks], f, indent=4)
            
    # def load_from_file(self):
    #     if os.path.exists(self.db_path):
    #         try:
    #             with open(self.db_path, 'r') as f:
    #                 data = json.load(f)
    #                 self.tasks = [Task.from_dict(item) for item in data]
    #         except (json.JSONDecodeError, ValueError):
    #             self.tasks = []