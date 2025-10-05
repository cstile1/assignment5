from app.calculator_memento import Caretaker

def test_empty_undo_redo_return_none():
    ct = Caretaker()
    assert ct.undo() is None
    assert ct.redo() is None
