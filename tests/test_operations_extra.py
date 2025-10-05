import pytest
from app.operations import make_operation
from app.exceptions import CalculatorError

def test_root_with_zero_root_raises():
    with pytest.raises(CalculatorError):
        make_operation("root").execute(9, 0)
