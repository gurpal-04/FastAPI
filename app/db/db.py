import json
from pathlib import Path
from threading import Lock

# Always points to app/db/tasks.json regardless of working directory
DB_FILE = Path(__file__).resolve().parent / "tasks.json"
_lock = Lock()

DEFAULT_DATA = {"users": [], "items": []}

def read_db() -> dict:
    with _lock:
        if not DB_FILE.exists():
            DB_FILE.write_text(json.dumps(DEFAULT_DATA, indent=2))
        return json.loads(DB_FILE.read_text())

def write_db(data: dict) -> None:
    with _lock:
        DB_FILE.write_text(json.dumps(data, indent=2))
