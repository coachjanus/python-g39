from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from .tasks import TaskList
from .priority import Priority
from .config import SUCCESS, ERRORS


class UI:
    def __init__(self, todo_list: TaskList) -> None:
        self.todo_list = todo_list
        self.console = Console()

    def display_menu(self) -> str:
        self.console.print("\n[bold cyan]--- To-Do App ---[/bold cyan]")
        self.console.print("1. View All Tasks")
        self.console.print("2. Add New Task")
        self.console.print("3. Mark Task as Completed")
        self.console.print("4. Remove Task")
        self.console.print("5. Change Priority")
        self.console.print("6. Exit")
        return Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "6"])

    def view(self) -> None:
        table = Table(title="To-Do List")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Description", style="green")
        table.add_column("Completed", justify="center")
        table.add_column("Priority", justify="center", style="yellow")

        for task in self.todo_list.get_tasks():
            status = "[green]✓[/green]" if task.completed else "[red]✗[/red]"
            table.add_row(str(task.id), task.description, status, Priority(task.priority).name)

        self.console.print(table)

    def choose_priority(self) -> Priority:
        options = " | ".join(f"{p.value}: {p.name}" for p in Priority)
        choice = Prompt.ask(
            f"Choose priority ({options})",
            choices=[str(p.value) for p in Priority],
            default=str(Priority.NORMAL.value),
        )
        return Priority(int(choice))

    def add(self) -> None:
        description = Prompt.ask("Enter task description")
        priority = self.choose_priority()
        response = self.todo_list.add_task(description, priority)
        if response.error == SUCCESS:
            self.console.print(f"[green]Task added:[/green] {response.todo}")
        else:
            self.console.print(f"[red]Error:[/red] {ERRORS[response.error]}")

    def complete(self) -> None:
        task_id = IntPrompt.ask("Enter task ID to mark as completed")
        response = self.todo_list.mark_completed(task_id)
        if not response:
            self.console.print(f"[red]No task found with ID: {task_id}[/red]")
        elif response.error == SUCCESS:
            self.console.print(f"[green]Completed:[/green] {response.todo}")

    def remove(self) -> None:
        task_id = IntPrompt.ask("Enter task ID to remove")
        response = self.todo_list.remove_task(task_id)
        if not response:
            self.console.print(f"[red]No task found with ID: {task_id}[/red]")
        elif response.error == SUCCESS:
            self.console.print(f"[yellow]Removed:[/yellow] {response.todo}")

    def new_priority(self) -> None:
        task_id = IntPrompt.ask("Enter task ID to change priority")
        priority = self.choose_priority()
        response = self.todo_list.set_priority(task_id, priority)
        if not response:
            self.console.print(f"[red]No task found with ID: {task_id}[/red]")
        elif response.error == SUCCESS:
            self.console.print(f"[green]Priority updated:[/green] {response.todo}")