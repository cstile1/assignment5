import os
from dotenv import load_dotenv
from .exceptions import ConfigError

def load_config() -> dict:
    load_dotenv()

    # Core settings
    autosave = os.getenv("CALCULATOR_AUTO_SAVE", "false").lower() in {"1","true","yes","on"}
    csv_path = os.getenv("CSV_PATH", "history.csv")
    max_history = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    if not csv_path:
        raise ConfigError("CSV_PATH cannot be empty")  # pragma: no cover
    if max_history <= 0:
        raise ConfigError("CALCULATOR_MAX_HISTORY_SIZE must be > 0")  # pragma: no cover

    return {
        "AUTOSAVE": autosave,
        "CSV_PATH": csv_path,
        "MAX_HISTORY": max_history,
        "ENCODING": encoding,
    }
