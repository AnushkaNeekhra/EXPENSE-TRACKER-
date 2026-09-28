import calendar
import os
import sys
from datetime import datetime
from typing import Dict, List

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from models.expense import Expense  # type: ignore[import-not-found]
    from utils.colors import green, red  # type: ignore[import-not-found]
except ModuleNotFoundError:
    try:
        from expense import Expense  # type: ignore[import-not-found]
        from colors import green, red  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        class Expense:
            def __init__(self, name: str, category: str, amount: float):
                self.name = name
                self.category = category
                self.amount = amount

        def green(value: str) -> str:
            return value

        def red(value: str) -> str:
            return value


class BudgetService:
    """Handles expense summaries and budget calculations."""

    @staticmethod
    def categorize_expenses(expenses: List[Expense]) -> Dict[str, float]:
        """Group total spending by expense category."""
        totals: Dict[str, float] = {}

        for expense in expenses:
            category = expense.category
            totals[category] = totals.get(category, 0.0) + expense.amount

        return totals

    @staticmethod
    def get_remaining_days_in_month() -> int:
        """Return the number of days left in the current month."""
        now = datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        return days_in_month - now.day + 1

    def display_summary(self, expenses: List[Expense], budget: float) -> None:
        """Display a clear monthly expense summary with remaining budget information."""
        if not expenses:
            print("\nNo expenses logged yet.")
            return

        print("\n" + "=" * 40)
        print(" EXPENSE SUMMARY REPORT ")
        print("=" * 40)

        category_totals = self.categorize_expenses(expenses)
        print("\nExpenses by Category:")
        for category, total in category_totals.items():
            print(f" • {category}: ${total:.2f}")

        total_spent = sum(expense.amount for expense in expenses)
        remaining_budget = budget - total_spent
        remaining_days = self.get_remaining_days_in_month()
        daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0.0

        print("\nFinancial Overview:")
        print(f" • Monthly Budget : ${budget:.2f}")
        print(f" • Total Spent    : ${total_spent:.2f}")

        if remaining_budget >= 0:
            print(f" • Budget Left    : {green(f'${remaining_budget:.2f}')}")
            print(f" • Daily Allowance: {green(f'${daily_budget:.2f}/day')} ({remaining_days} days left)")
        else:
            print(f" • Budget Deficit : {red(f'${abs(remaining_budget):.2f}')} (Over Budget!)")

        print("=" * 40)