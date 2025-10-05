import pandas as pd
from typing import List, Optional

class Memento:
    def __init__(self, df: pd.DataFrame) -> None:
        # store an immutable snapshot (copy)
        self._df = df.copy()

    def state(self) -> pd.DataFrame:
        # return a fresh copy so callers can't mutate internal state
        return self._df.copy()

class Caretaker:
    def __init__(self) -> None:
        self._undo: List[Memento] = []
        self._redo: List[Memento] = []

    def push(self, m: Memento) -> None:
        self._undo.append(m)
        self._redo.clear()

    def undo(self) -> Optional[Memento]:
        if not self._undo:
            return None
        m = self._undo.pop()
        self._redo.append(m)
        return m

    def redo(self) -> Optional[Memento]:
        if not self._redo:
            return None
        m = self._redo.pop()
        self._undo.append(m)
        return m
