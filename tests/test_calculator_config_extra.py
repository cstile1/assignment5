import pytest
from app.calculator_config import load_config
from app.exceptions import ConfigError

def test_defaults_when_env_missing(monkeypatch):
    monkeypatch.delenv("AUTOSAVE", raising=False)
    monkeypatch.delenv("CSV_PATH", raising=False)
    cfg = load_config()
    assert cfg["AUTOSAVE"] is False
    assert cfg["CSV_PATH"] == "history.csv"

def test_empty_csv_path_errors(monkeypatch):
    monkeypatch.setenv("CSV_PATH", "")
    with pytest.raises(ConfigError):
        load_config()
