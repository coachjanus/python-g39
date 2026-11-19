from pathlib import Path
import json, os
from .model import Task
from typing import List
from .responses import DBResponse, TodoResponse
from .config import SUCCESS, DB_WRITE_ERROR, JSON_ERROR, DB_READ_ERROR

class DBHandler:
    """Handles JSON storage I/O and disk-write exceptions."""
    
    def __init__(self, db_path: Path)-> None:
        self.db_path = db_path
        
    def save_to_file(self, todo_list: List[Task])->DBResponse:
        """Saves the task list to the JSON database."""
        try:
            with open(self.db_path, 'w') as f:
                json.dump([task.to_dict() for task in todo_list], f, indent=4)
            return  DBResponse(todo_list, SUCCESS)
        except OSError as e:
            return DBResponse(todo_list, DB_WRITE_ERROR)
    
    def load_from_file(self)->DBResponse:
        """Retrieves the task list from the JSON database."""
        try:
            if os.path.exists(self.db_path):
                try:
                    with open(self.db_path, 'r') as f:
                        data = json.load(f)
                        try:
                            self.tasks = [Task.from_dict(item) for item in data]
                            return  DBResponse(self.tasks, SUCCESS)
                        except json.JSONDecodeError as e:
                            return DBResponse([], JSON_ERROR)
                except OSError as e:
                    return DBResponse([], DB_READ_ERROR)
        except OSError as e:
            return DBResponse([], DB_READ_ERROR)  

