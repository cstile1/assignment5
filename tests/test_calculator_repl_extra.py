from app.calculator_repl import CalculatorFacade
from app.exceptions import InvalidOperation
import pytest

def test_autosave_observer_added(monkeypatch, tmp_path):
    # Exercise the AUTOSAVE branch that attaches an observer
    monkeypatch.setenv("AUTOSAVE", "true")
    monkeypatch.setenv("CSV_PATH", str(tmp_path / "hist.csv"))
    c = CalculatorFacade()
    # verify observer attached
    assert hasattr(c.history, "_observers")
    assert len(c.history._observers) == 1  # type: ignore[attr-defined]

def test_undo_redo_when_empty():
    # With no snapshots, undo/redo should be False
    c = CalculatorFacade()
    assert c.undo() is False
    assert c.redo() is False

def test_invalid_operation_raises(monkeypatch):
    monkeypatch.setenv("AUTOSAVE", "false")
    c = CalculatorFacade()
    with pytest.raises(InvalidOperation):
        c.compute("nope", 1, 2)
