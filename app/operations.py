from typing import Protocol

class Operation(Protocol):
    name: str
    def execute(self, a: float, b: float) -> float: ...

class Add:
    name = "add"
    def execute(self, a, b): return a + b

class Sub:
    name = "sub"
    def execute(self, a, b): return a - b

class Mul:
    name = "mul"
    def execute(self, a, b): return a * b

class Div:
    name = "div"
    def execute(self, a, b):
        if b == 0:
            from .exceptions import DivisionByZero
            raise DivisionByZero("Cannot divide by zero")
        return a / b

class Pow:
    name = "pow"
    def execute(self, a, b): return a ** b

class Root:
    name = "root"
    def execute(self, a, b):
        # b-th root of a -> a ** (1/b)
        if b == 0:
            from .exceptions import CalculatorError
            raise CalculatorError("Zero root is undefined")
        return a ** (1.0 / b)

# Factory
def make_operation(op_name: str) -> Operation:
    table = {
        "add": Add, "sub": Sub, "mul": Mul, "div": Div, "pow": Pow, "root": Root
    }
    try:
        return table[op_name]()  # type: ignore[call-arg]
    except KeyError:
        from .exceptions import InvalidOperation
        raise InvalidOperation(f"Unsupported operation: {op_name}")
