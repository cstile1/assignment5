# Enhanced Calculator (IS601 Assignment 5)

This is a Python command-line calculator with:
- REPL (Read-Eval-Print-Loop)
- Arithmetic operations: add, sub, mul, div, pow, root
- History with pandas (save/load to CSV)
- Undo/redo using Memento pattern
- Configurable with `.env`
- 100% test coverage (pytest + GitHub Actions)

---

## Setup

# create & activate venv
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the project root:

CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_DEFAULT_ENCODING=utf-8
CSV_PATH=history.csv

---

## Usage

Run the REPL:

python -m app.calculator_repl

Example:

>> add 2 3
>> pow 2 5
>> history
>> undo
>> redo
>> save
>> exit

---

## Testing

pytest --cov=app --cov-branch

- All tests must pass   
- Coverage must stay at **100%** 

---

## Design Patterns Used

- **Strategy**: arithmetic operations  
- **Factory**: create operations  
- **Observer**: autosave/logging  
- **Memento**: undo/redo  
- **Facade**: CalculatorFacade entry point  
