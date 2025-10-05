from app.calculator_config import load_config

def test_load_config_env(monkeypatch):
    monkeypatch.setenv("AUTOSAVE", "true")
    monkeypatch.setenv("CSV_PATH", "x.csv")
    cfg = load_config()
    assert cfg["AUTOSAVE"] is True
    assert cfg["CSV_PATH"] == "x.csv"
