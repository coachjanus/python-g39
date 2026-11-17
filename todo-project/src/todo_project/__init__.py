'''Todo Project: Top level module for todo application'''

from pathlib import Path

import typer

from todo_project import config

from .ui import UI
from .database import init_database


# from .cli import cli  # pyright: ignore[reportMissingImports]

app = typer.Typer()

@app.command()
def init(db_path: str = typer.Option(str(config.DEFAULT_DB_FILE_PATH), prompt="TODO database location?")):
    """Initialize the todo CLI application."""
    
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(f"Creating config file failed with {config.ERRORS[app_init_error]}", fg=typer.colors.RED)
        raise typer.Exit(1)
    db_init_error = init_database(Path(db_path))
    if db_init_error:
        typer.secho(f"Creating database failed with {config.ERRORS[db_init_error]}", fg=typer.colors.RED)
        raise typer.Exit(1)
    typer.secho(f"The todo database is {db_path}", fg=typer.colors.GREEN)

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
                    print("task_id:", task_id)
                    # new_priority = input("Enter new priority (low, medium, high): ")
                    # ui.change_priority(task_id, new_priority)
                    ui.new_priority(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            case '6':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.") 
            
def main() -> None:
    app()
