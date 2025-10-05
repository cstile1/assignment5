from app.calculation import Calculation
from app.operations import make_operation

def test_calculation_result():
    c = Calculation(2, 5, make_operation("mul"))
    assert c.result() == 10
