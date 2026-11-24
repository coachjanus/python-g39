import json
from pathlib import Path
from typing import List
from .model import Task
from .responses import DBResponse
from .config import SUCCESS, DB_WRITE_ERROR, JSON_ERROR, DB_READ_ERROR

class DBHandler:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
    # Атомарний запис у файл: При записі напряму у файл (open(self.db_path, 'w')), якщо програма аварійно завершиться під час запису, файл бази даних обнулиться і всі задачі зникнуть. Краще записувати у тимчасовий файл і замінювати основний через os.replace().
    # Вказуйте кодування encoding="utf-8": 
    # Завжди додавайте encoding="utf-8" при відкритті файлів (особливо на Windows), інакше кирилиця в описах задач збережеться у вигляді \u041f\u0440... або викличе UnicodeEncodeError.
    # Прибрати indent=4 у продакшені (опціонально): Якщо задач стане тисячі, форматування з відступами збільшує розмір файлу і час парсингу. Для великих списків краще писати компактний JSON або перейти на вбудований sqlite3.
    def save_to_file(self, todo_list: List[Task]) -> DBResponse:
        try:
            with self.db_path.open("w", encoding="utf-8") as f:
                json.dump([task.to_dict() for task in todo_list], f, ensure_ascii=False, indent=2)
            return DBResponse(todo_list, SUCCESS)
        except OSError:
            return DBResponse(todo_list, DB_WRITE_ERROR)

    # Прибрати глибоку вкладеність try-except: У load_from_file три рівні вкладеності, а json.JSONDecodeError перехоплюється вже після json.load(f) (помилка виникне саме на рядку json.load(f), тому внутрішній try її не зловить!). Об'єднайте все в один плоский блок try ... except (OSError, json.JSONDecodeError).
    def load_from_file(self) -> DBResponse:
        if not self.db_path.exists():
            return DBResponse([], DB_READ_ERROR)
        try:
            with self.db_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            tasks = [Task.from_dict(item) for item in data]
            return DBResponse(tasks, SUCCESS)
        except json.JSONDecodeError:
            return DBResponse([], JSON_ERROR)
        except (OSError, KeyError, ValueError):
            return DBResponse([], DB_READ_ERROR)