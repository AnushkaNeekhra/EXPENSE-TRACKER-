import os
from typing import List

try:
    from models.expense import Expense  # type: ignore[import-not-found]
except ModuleNotFoundError:
    try:
        from expense import Expense  # type: ignore[import-not-found]
    except ModuleNotFoundError:  # pragma: no cover - fallback for IDE/static analysis
        class Expense:  # type: ignore[no-redef]
            def __init__(self, name: str, amount: float, category: str):
                self.name = name
                self.amount = amount
                self.category = category


class FileService:
        #Handles reading and writing expense data to CSV storage.

    def __init__(self, filepath: str = "expenses.csv"):
        self.filepath = filepath

    def save_expense(self, expense: Expense) -> None:
       #Appends a new expense record to the CSV file.
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"{expense.name},{expense.amount},{expense.category}\n")
        print(f"Saved: {expense.name} (${expense.amount:.2f}) to {self.filepath}")

    def load_expenses(self) -> List[Expense]:
        """Reads all expenses from the CSV file and returns a list of Expense objects."""
        expenses: List[Expense] = []

        if not os.path.exists(self.filepath):
            return expenses

        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                parts = stripped.split(",")
                if len(parts) == 3:
                    name, amount_str, category = parts
                    try:
                        expense = Expense(
                            name=name,
                            category=category,
                            amount=float(amount_str)
                        )
                        expenses.append(expense)
                    except ValueError:
                        continue # Skip corrupted rows gracefully
        return expenses
