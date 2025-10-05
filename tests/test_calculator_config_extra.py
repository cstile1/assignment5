import pytest
from app.calculator_config import load_config
from app.exceptions import ConfigError

def test_defaults_and_new_vars(monkeypatch):
    # Explicitly override the .env value so tests are deterministic
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")

    # Remove others so defaults apply (or .env doesn't override them)
    monkeypatch.delenv("CSV_PATH", raising=False)
    monkeypatch.delenv("CALCULATOR_MAX_HISTORY_SIZE", raising=False)
    monkeypatch.delenv("CALCULATOR_DEFAULT_ENCODING", raising=False)

    cfg = load_config()
    assert cfg["AUTOSAVE"] is False           # forced to false for the test
    assert cfg["CSV_PATH"] == "history.csv"   # default
    assert cfg["MAX_HISTORY"] == 100          # default (same as your .env anyway)
    assert cfg["ENCODING"] == "utf-8"         # default (same as your .env)

def test_invalid_max_history(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "0")
    with pytest.raises(ConfigError):
        load_config()
