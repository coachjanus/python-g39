import os
import time
import threading
from pathlib import Path
from typing import Iterator, Dict


def get_directory_state(path: str) -> Dict[str, float]:
    """
    Returns a dictionary mapping file paths to their last modification times.
    """
    state = {}
    dirs_to_scan = [path]
    
    while dirs_to_scan:
        current_dir = dirs_to_scan.pop()
        try:
            with os.scandir(current_dir) as it:
                for entry in it:
                    try:
                        if entry.is_dir():
                            if not entry.is_symlink():
                                dirs_to_scan.append(entry.path)
                        else:
                            # Store the modification time
                            state[entry.path] = entry.stat().st_mtime
                    except OSError:
                        # File might have been deleted or we might not have permission
                        pass
        except OSError:
            pass
            
    return state


def watch_directory(path: str, poll_interval: float = 1.0, stop_event: threading.Event = None) -> Iterator[Dict[str, str]]:
    """
    Monitors a directory for changes (creation, modification, deletion) and yields events.
    """
    path_obj = Path(path)
    if not path_obj.exists() or not path_obj.is_dir():
        raise ValueError(f"Path '{path}' is not a valid directory.")
        
    if stop_event is None:
        stop_event = threading.Event()

    print(f"Starting to monitor directory: {path}")

    # Initial state snapshot
    current_state = get_directory_state(path)

    while not stop_event.is_set():
        time.sleep(poll_interval)
        
        # Get new state snapshot
        new_state = get_directory_state(path)
        
        # Check for created or modified files
        for file_path, mtime in new_state.items():
            if file_path not in current_state:
                yield {"event": "created", "path": file_path}
            elif current_state[file_path] < mtime:
                yield {"event": "modified", "path": file_path}
                
        # Check for deleted files
        for file_path in current_state.keys():
            if file_path not in new_state:
                yield {"event": "deleted", "path": file_path}
                
        # Update current state
        current_state = new_state
