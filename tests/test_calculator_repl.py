from app.calculator_repl import CalculatorFacade

def test_facade_compute_and_undo_redo(monkeypatch, tmp_path):
    # ensure autosave is off for test determinism
    monkeypatch.setenv("AUTOSAVE", "false")
    monkeypatch.setenv("CSV_PATH", str(tmp_path / "hist.csv"))
    c = CalculatorFacade()

    # compute and check history
    r = c.compute("add", 1, 2)
    assert r == 3
    assert len(c.history.dataframe) == 1

    # undo/redo
    assert c.undo() is True
    assert len(c.history.dataframe) == 1  # undo restores snapshot state; here it's the same row shape
    assert c.redo() is True

    # save/load
    path = str(tmp_path / "out.csv")
    c.save(path)
    c.load(path)
