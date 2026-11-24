# src/todo_project/priority.py
from enum import IntEnum

class Priority(IntEnum):
    NORMAL = 0
    IMPORTANT = 1
    CRITICAL = 2
    
    # def from_name(cls, name: str) -> int:
    #     # Get the raw integer value
    #     return Priority[name].value
    
    # @classmethod
    # def from_name(cls, name: str) -> int:
    #     # Use brackets [] for name lookup, and .upper() to handle lowercase inputs
    #     return cls[name.upper()].value
    
    @classmethod
    def from_name(cls, name: str) -> int:
        try:
            return cls[name.upper()].value
        except KeyError:
            raise ValueError(f"Invalid priority name: {name!r}") from None