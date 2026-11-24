import json
from pathlib import Path
from todo_project.dbhandler import DBHandler
from todo_project.model import Task
from todo_project.priority import Priority
from todo_project.config import SUCCESS, DB_READ_ERROR, JSON_ERROR


def test_save_and_load_tasks(tmp_path: Path) -> None:
    db_file = tmp_path / "test_todo.json"
    handler = DBHandler(db_file)
    tasks = [
        Task(id=1, description="Купити молоко", priority=Priority.NORMAL),
        Task(id=2, description="Зробити рефакторинг", priority=Priority.CRITICAL, completed=True),
        ]
    save_res = handler.save_to_file(tasks)
    assert save_res.error == SUCCESS
    assert db_file.exists()
    load_res = handler.load_from_file()
    assert load_res.error == SUCCESS
    assert len(load_res.data) == 2
    assert load_res.data[0].description == "Купити молоко"
    assert load_res.data[1].priority == Priority.CRITICAL
    assert load_res.data[1].completed is True
    
    
def test_load_nonexistent_file(tmp_path: Path) -> None:
    handler = DBHandler(tmp_path / "missing.json")
    res = handler.load_from_file()
    assert res.error == DB_READ_ERROR
    assert res.data == []
    
def test_load_corrupted_json(tmp_path: Path) -> None:
    db_file = tmp_path / "corrupted.json"
    db_file.write_text("{invalid json", encoding="utf-8")
    handler = DBHandler(db_file)
    res = handler.load_from_file()
    assert res.error == JSON_ERROR
    assert res.data == []