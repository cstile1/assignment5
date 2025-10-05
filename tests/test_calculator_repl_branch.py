from app.calculator_repl import CalculatorFacade

def test_no_observer_when_autosave_false(monkeypatch):
    # Force AUTOSAVE off to cover the 'False' branch in __init__
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    c = CalculatorFacade()
    assert hasattr(c.history, "_observers")
    assert len(c.history._observers) == 0  # type: ignore[attr-defined]
