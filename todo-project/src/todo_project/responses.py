from typing import NamedTuple, Dict, Any, TypeAlias, List

# TodoListDict

TodoListDict: TypeAlias = List[Dict[str, Any]]


class DBResponse(NamedTuple):
    data: TodoListDict
    error: int

class TodoResponse(NamedTuple):
    todo: Dict[str, Any]
    error: int