'''Todo Project: Top level module for todo application'''

import logging
from pathlib import Path
import typer

from todo_project import config
from .database import init_database, get_database_path
from .tasks import TaskList
from .ui import UI

app = typer.Typer()

# logging.basicConfig(...) на рівні імпорту модуля створюватиме файл todo.log у поточній директорії навіть при звичайному запуску --help або при імпорті пакету в тестах. 
# Перенесіть налаштування логування всередину команди start() або у конфігураційну директорію CONFIG_DIR_PATH.
def _setup_logging() -> None:
    """Configure logging inside the application config directory."""
    config.CONFIG_DIR_PATH.mkdir(parents=True, exist_ok=True)
    log_file = config.CONFIG_DIR_PATH / "todo.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def _get_task_list() -> TaskList:
    """Validate config and database existence, then return initialized TaskList."""
    if not config.CONFIG_FILE_PATH.exists():
        typer.secho("Config file not found. Please run 'todo init'", fg=typer.colors.RED)
        raise typer.Exit(1)

    db_path = get_database_path(config.CONFIG_FILE_PATH)
    if not db_path.exists():
        typer.secho("Database not found. Please run 'todo init'", fg=typer.colors.RED)
        raise typer.Exit(1)

    return TaskList(db_path)


@app.command()
def init(
    db_path: str = typer.Option(
        str(config.DEFAULT_DB_FILE_PATH),
        prompt="TODO database location?",
    )
) -> None:
    """Initialize the todo CLI application."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f"Creating config file failed with {config.ERRORS[app_init_error]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    db_init_error = init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f"Creating database failed with {config.ERRORS[db_init_error]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    typer.secho(f"The todo database is {db_path}", fg=typer.colors.GREEN)

# Винесіть отримання ID у допоміжну функцію _prompt_task_id(prompt_text: str) -> int | None. 
@app.command()
def start() -> None:
    """Main application entry point for the todo CLI."""
    _setup_logging()
    task_list = _get_task_list()
    ui = UI(task_list)

    actions = {
        "1": ui.view,
        "2": ui.add,
        "3": ui.complete,
        "4": ui.remove,
        "5": ui.new_priority,
    }

    while True:
        choice = ui.display_menu()
        if choice == "6":
            typer.secho("Exiting the application. Goodbye!", fg=typer.colors.CYAN)
            break

        action = actions.get(choice)
        if action:
            action()
            logging.debug(f"Executed menu action: {choice}")
        else:
            typer.secho("Invalid choice. Please enter a number between 1 and 6.", fg=typer.colors.RED)


def main() -> None:
    app()
