from dataclasses import dataclass
from .operations import Operation

@dataclass(frozen=True)
class Calculation:
    a: float
    b: float
    op: Operation

    def result(self) -> float:
        return self.op.execute(self.a, self.b)
