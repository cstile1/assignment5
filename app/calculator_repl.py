from .operations import make_operation
from .calculation import Calculation
from .history import History, Observer
from .calculator_memento import Memento, Caretaker
from .calculator_config import load_config
from .input_validators import parse_two_floats

class AutosaveObserver(Observer):  # pragma: no cover
    def __init__(self, path: str) -> None:
        self.path = path
    def on_calculation(self, calc, result) -> None:  # pragma: no cover
        # Kept minimal; we trigger saves from the facade after record
        pass

class CalculatorFacade:
    def __init__(self) -> None:
        self.config = load_config()
        self.history = History()
        self.caretaker = Caretaker()
        if self.config["AUTOSAVE"]:
            self.history.add_observer(AutosaveObserver(self.config["CSV_PATH"]))

    def snapshot(self):
        self.caretaker.push(Memento(self.history.dataframe))

    def compute(self, op_name: str, a: float, b: float) -> float:
        # compute result
        calc = Calculation(a, b, make_operation(op_name))
        res = calc.result()
        # record into history
        self.history.record(calc, res)
        # snapshot AFTER recording so undo restores this state
        self.snapshot()
        return res

    def undo(self) -> bool:
        m = self.caretaker.undo()
        if not m:
            return False
        self.history._df = m.state()
        return True

    def redo(self) -> bool:
        m = self.caretaker.redo()
        if not m:
            return False
        self.history._df = m.state()
        return True

    def save(self, path: str) -> None:
        self.history.save_csv(path)

    def load(self, path: str) -> None:
        self.snapshot()
        self.history.load_csv(path)

def main():  # pragma: no cover
    calc = CalculatorFacade()
    print("Enhanced Calculator. Type 'help' for commands. 'exit' to quit.")
    while True:
        line = input(">> ").strip()
        if not line:
            continue
        cmd, *rest = line.split()
        if cmd in {"exit", "quit"}:
            break
        if cmd == "help":
            print("Commands: add|sub|mul|div|pow|root a b | history | clear | undo | redo | save [path] | load [path] | help | exit")
            continue
        if cmd == "history":
            print(calc.history.dataframe)
            continue
        if cmd == "clear":
            calc.snapshot()
            calc.history.clear()
            print("Cleared.")
            continue
        if cmd == "undo":
            print("Undone." if calc.undo() else "Nothing to undo.")
            continue
        if cmd == "redo":
            print("Redone." if calc.redo() else "Nothing to redo.")
            continue
        if cmd == "save":
            path = rest[0] if rest else calc.config["CSV_PATH"]
            calc.save(path)
            print(f"Saved to {path}")
            continue
        if cmd == "load":
            path = rest[0] if rest else calc.config["CSV_PATH"]
            calc.load(path)
            print(f"Loaded from {path}")
            continue

        try:
            a, b = parse_two_floats([cmd, *rest])
            result = calc.compute(cmd, a, b)
            if calc.config["AUTOSAVE"]:
                calc.save(calc.config["CSV_PATH"])
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":  # pragma: no cover
    main()
