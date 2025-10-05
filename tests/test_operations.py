import pytest
from app.operations import make_operation
from app.exceptions import DivisionByZero, InvalidOperation

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 1, 2, 3),
    ("sub", 5, 3, 2),
    ("mul", 4, 2, 8),
    ("div", 8, 2, 4),
    ("pow", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_ops(op, a, b, expected):
    o = make_operation(op)
    assert o.execute(a, b) == pytest.approx(expected)

def test_div_zero():
    with pytest.raises(DivisionByZero):
        make_operation("div").execute(1, 0)

def test_invalid_op():
    with pytest.raises(InvalidOperation):
        make_operation("nope")
