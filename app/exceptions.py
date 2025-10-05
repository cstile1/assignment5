class CalculatorError(Exception):
    """Base calculator error."""

class InvalidOperation(CalculatorError):
    """Unsupported operation."""

class DivisionByZero(CalculatorError):
    """Division by zero."""

class ConfigError(CalculatorError):
    """Bad configuration."""
