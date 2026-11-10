from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from todo_project.tasks import TaskList
from .model import Task
from .priority import Priority

class UI:
    def __init__(self):
        self.todo_list = TaskList()
        self.console = Console()

    def display_menu(self):
        print("\n--- To-Do App ---")
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Change priority")
        print("6. Exit")
        return input("\nEnter your choice (1-6): ")
    
    def view(self):
        # Display all tasks in a table format
        table = Table(title="To-Do List")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Completed", justify="center", style="red")
        table.add_column("Priority", justify="center", style="yellow")

        # Assuming self.todo_list.get_tasks() returns a list of Task objects
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            table.add_row(str(task.id), task.title, task.description, str(task.completed), task.priority.name)

        self.console.print(table)
        
    def add(self, description):
        # Add a new task with the given description
        task_id = 1 if not self.todo_list.get_tasks() else max(t.id for t in self.todo_list.get_tasks()) + 1
        new_task = Task(id=task_id, title=description, description=description)
        self.todo_list.add_task(new_task)
        print(f"Task added: {new_task}")
        
    def complete(self, task_id):
        # Mark a task as completed based on the given task_id
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task marked as completed: {task}")
                return
        print(f"No task found with ID: {task_id}")
        
    def remove(self, task_id):
        # Remove a task based on the given task_id
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            if task.id == task_id:
                self.todo_list.remove_task(task)
                print(f"Task removed: {task}")
                return
        print(f"No task found with ID: {task_id}")
        
    def change_priority(self, task_id, new_priority):
        # Change the priority of a task based on the given task_id
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            if task.id == task_id:
                task.priority = new_priority
                print(f"Task priority changed: {task}")
                return
        print(f"No task found with ID: {task_id}")
    