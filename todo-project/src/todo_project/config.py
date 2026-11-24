import configparser
from pathlib import Path
import typer

__app_name__ = "todo"
version = "0.1.0"

# коди повернення за допомогою range() призначаємо їм цілі числа.
(
SUCCESS,
DIR_ERROR,
FILE_ERROR,
DB_READ_ERROR,
DB_WRITE_ERROR,
JSON_ERROR,
ID_ERROR,
) = range(7)

ERRORS = {
DIR_ERROR: "config directory error",
FILE_ERROR: "config file error",
DB_READ_ERROR: "database read error",
DB_WRITE_ERROR: "database write error",
JSON_ERROR: "JSON-file ERROR",
ID_ERROR: "to-do id error",
}

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / 'config.ini'
DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_todo.json")

def _init_config_file():
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS

def _create_database(db_path):
    config_parser = configparser.ConfigParser()
    config_parser['General'] = {"database": db_path}
    try:
        with CONFIG_FILE_PATH.open('w') as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS

def init_app(db_path):
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    return SUCCESS