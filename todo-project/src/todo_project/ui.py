from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import typer

from todo_project import config
from todo_project.database import get_database_path
from todo_project.tasks import TaskList
from .model import Task
from .priority import Priority

class UI:
    def __init__(self):
        self.todo_list = self.get_tasks()
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

        table.add_column("Description", style="green")
        table.add_column("Completed", justify="center", style="red")
        table.add_column("Priority", justify="center", style="yellow")

        # Assuming self.todo_list.get_tasks() returns a list of Task objects
        tasks = self.todo_list.get_tasks()
        for task in tasks:

            table.add_row(str(task.id), task.description, str(task.completed), Priority(task.priority).name)

        self.console.print(table)
        
    def get_tasks(self):
        if config.CONFIG_FILE_PATH.exists():
            db_path = get_database_path(config.CONFIG_FILE_PATH)
        else:
            typer.secho("Config file not found. Please run todo init", fg=typer.colors.RED)
            raise typer.Exit(1)
        if db_path.exists():
            return TaskList(db_path)
        else:
            typer.secho("Database not found. Please run todo init", fg=typer.colors.RED)
            raise typer.Exit(1)
        
    def add(self, description):
        # Add a new task with the given description
        
        priority=self.choose_priority()
        new_task = self.todo_list.add_task(description, int(priority))
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
    
    @staticmethod
    def join_priority():
        res = ""
        for priority in Priority:
            res += f" {priority.value}: {priority.name}"
        return res
    
    def choose_priority(self):
        return Prompt.ask("Coose priority: " + UI.join_priority(), choices=[str(priority.value) for priority in Priority], default="0")
    
    def new_priority(self, task_id):
        priority = Priority(int(self.choose_priority()))
        
        if self.todo_list.set_priority(task_id, int(priority)):
            self.console.print("Task changed priority.", style="bold green")
        else:
            self.console.print("Task not found.", style="bold red")
            
