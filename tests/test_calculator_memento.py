from app.calculator_memento import Memento, Caretaker
import pandas as pd

def test_undo_redo():
    df = pd.DataFrame({"a":[1], "op":["Add"], "b":[2], "result":[3]})
    m = Memento(df)
    ct = Caretaker()
    ct.push(m)

    m1 = ct.undo()
    assert m1 is not None
    # simulate restoring state
    restored = m1.state()
    assert list(restored.columns) == ["a", "op", "b", "result"]

    m2 = ct.redo()
    assert m2 is not None
    restored2 = m2.state()
    assert restored2.equals(restored)
