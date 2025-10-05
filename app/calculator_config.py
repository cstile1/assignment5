import os
from dotenv import load_dotenv
from .exceptions import ConfigError

def load_config() -> dict:
    load_dotenv()
    autosave = os.getenv("AUTOSAVE", "false").lower() in {"1","true","yes","on"}
    csv_path = os.getenv("CSV_PATH", "history.csv")
    if not csv_path:
        raise ConfigError("CSV_PATH cannot be empty")  # pragma: no cover
    return {"AUTOSAVE": autosave, "CSV_PATH": csv_path}
