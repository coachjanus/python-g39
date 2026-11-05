
from todo_project.tasks import TaskList

from .config import version, app_name
from .model import Task
from .tasks import TaskList

def app() -> None:
    """Main entry point for the todo application."""
    print(f"Welcome to {app_name} version {version}!")
    task_list = TaskList()
    
    # print(dir(task_list))
    # print(task_list.__class__)
    
    task1 = Task(id=1, title="Buy groceries", description="Milk, Bread, Eggs")
    task2 = Task(id=2, title="Read a book", description="Finish reading 'The Great Gatsby'")

    task_list.add_task(task1)
    task_list.add_task(task2)
    
    tasks = task_list.get_tasks()
    
    task_id = 1 if not tasks else max(t.id for t in tasks) + 1
    
    print(f"Next task ID: {task_id}")
    task3 = Task(id=task_id, title="Exercise", description="Go for a 30-minute run")
    task_list.add_task(task3)
    
    for task in tasks:
        print(task)
    
    
    # task1.mark_completed()
    task_id = 2
    
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task marked as completed: {task}")

    for task in tasks:
        print(task)