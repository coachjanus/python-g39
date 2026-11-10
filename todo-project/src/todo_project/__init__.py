'''Todo Project: Top level module for todo application'''

import typer

from .ui import UI


from .cli import cli  # pyright: ignore[reportMissingImports]

app = typer.Typer()

@app.command()
def init():
    """Initialize the todo CLI application."""
    print("Todo CLI Application Initialized")

@app.command()
def start():
    """Main application entry point for the todo CLI."""
    # cli()  # Call the cli function from cli.py
    ui = UI()
    while True:
        choice = ui.display_menu()
        match choice:
            case '1':
                ui.view()
            case '2':
                description = input("Enter task description: ")
                ui.add(description)
            case '3':
                try:
                    task_id = int(input("Enter task ID to mark as completed: "))
                    ui.complete(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            case '4':
                try:
                    task_id = int(input("Enter task ID to remove: "))
                    ui.remove(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            case '5':
                try:
                    task_id = int(input("Enter task ID to change priority: "))
                    new_priority = input("Enter new priority (low, medium, high): ")
                    ui.change_priority(task_id, new_priority)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            case '6':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.") 
            
def main() -> None:
    app()
