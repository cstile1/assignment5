import pandas as pd
from typing import List, Protocol
from .calculation import Calculation

class Observer(Protocol):
    def on_calculation(self, calc: Calculation, result: float) -> None: ...

class History:
    def __init__(self) -> None:
        # columns: a, op class name, b, and the numeric result
        self._df = pd.DataFrame(columns=["a", "op", "b", "result"])
        self._observers: List[Observer] = []

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._df

    def add_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def record(self, calc: Calculation, result: float) -> None:
        self._df.loc[len(self._df)] = [calc.a, type(calc.op).__name__, calc.b, result]
        for obs in self._observers:
            obs.on_calculation(calc, result)

    def clear(self) -> None:
        self._df = self._df.iloc[0:0]

    def save_csv(self, path: str) -> None:
        self._df.to_csv(path, index=False)

    def load_csv(self, path: str) -> None:
        self._df = pd.read_csv(path)
