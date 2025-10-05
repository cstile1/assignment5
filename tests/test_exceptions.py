from app.exceptions import CalculatorError, InvalidOperation, DivisionByZero, ConfigError

def test_exception_types():
    assert issubclass(InvalidOperation, CalculatorError)
    assert issubclass(DivisionByZero, CalculatorError)
    assert issubclass(ConfigError, CalculatorError)
