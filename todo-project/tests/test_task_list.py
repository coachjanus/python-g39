import pytest
from pathlib import Path
from todo_project.tasks import TaskList
from todo_project.priority import Priority
from todo_project.config import SUCCESS


@pytest.fixture
def task_list(tmp_path: Path) -> TaskList:
    """Fixture providing a TaskList backed by a temporary empty JSON database."""
    db_file = tmp_path / "tasks.json"
    db_file.write_text("[]", encoding="utf-8")
    return TaskList(db_file)


def test_add_task_and_persistence(tmp_path: Path) -> None:
    db_file = tmp_path / "tasks.json"
    db_file.write_text("[]", encoding="utf-8")
    tl = TaskList(db_file)
    res = tl.add_task("Вивчити pytest", Priority.IMPORTANT)
    assert res.error == SUCCESS
    assert res.todo.id == 1
    assert len(tl.get_tasks()) == 1
    # Перевіряємо, що дані реально збереглися у файл
    reloaded_tl = TaskList(db_file)
    tasks = reloaded_tl.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].description == "Вивчити pytest"
    assert tasks[0].priority == Priority.IMPORTANT
    
    
def test_id_generation_after_deletion(task_list: TaskList) -> None:
    task_list.add_task("Задача 1")
    task_list.add_task("Задача 2")
    task_list.remove_task(1)
    res = task_list.add_task("Задача 3")
    # Новий ID має бути 3, а не 2 (без колізій)
    assert res.todo.id == 3


def test_mark_completed(task_list: TaskList) -> None:
    task_list.add_task("Написати тести")
    res = task_list.mark_completed(1)
    assert res is not None
    assert res.error == SUCCESS
    assert res.todo.completed is True
    assert task_list.mark_completed(999) is None


def test_set_priority(task_list: TaskList) -> None:
    task_list.add_task("Оновити залежності", Priority.NORMAL)
    res = task_list.set_priority(1, Priority.CRITICAL)
    assert res is not None
    assert res.error == SUCCESS
    assert res.todo.priority == Priority.CRITICAL
    assert task_list.set_priority(999, Priority.IMPORTANT) is None
    
def test_remove_task(task_list: TaskList) -> None:
    task_list.add_task("Тимчасова задача")
    res = task_list.remove_task(1)
    assert res is not None
    assert res.error == SUCCESS
    assert len(task_list.get_tasks()) == 0
    assert task_list.remove_task(1) is None    