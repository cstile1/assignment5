from app.history import History
from app.calculation import Calculation
from app.operations import make_operation

def test_record_and_save_load(tmp_path):
    h = History()
    calc = Calculation(2, 3, make_operation("add"))
    h.record(calc, 5)
    assert len(h.dataframe) == 1
    # save
    p = tmp_path / "hist.csv"
    h.save_csv(str(p))
    # clear and load back
    h.clear()
    assert len(h.dataframe) == 0
    h.load_csv(str(p))
    assert len(h.dataframe) == 1
    assert list(h.dataframe.columns) == ["a", "op", "b", "result"]
