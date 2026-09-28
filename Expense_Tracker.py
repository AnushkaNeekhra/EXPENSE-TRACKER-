import calendar
from datetime import datetime
from typing import Dict, List

from Expense import Expense


def main():
    print("💰 Running Expense Tracker!")
    expense_file_name = "expenses_record.csv"

    while True:
        expense = add_expense()
        save_expense_to_file(expense, expense_file_name)

        while True:
            choice = input("Do you want to add another expense? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                break
            if choice in ("n", "no"):
                calculate_summary(expense_file_name)
                return
            print("Please enter 'y' for yes or 'n' for no.")


def add_expense():
    print("💰 Getting user expense details")

    while True:
        expense_name = input("Enter your expense name: ").strip()
        if expense_name:
            break
        print("Expense name cannot be empty. Please try again.")

    while True:
        try:
            expense_amount = float(input("Enter your expense amount: "))
            if expense_amount >= 0:
                break
            print("Amount must be zero or greater.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    expense_categories = [
        "🛒Groceries",
        "🛍️👕👗Shopping",
        "🏢Work",
        "🎆Entertainment",
        "🏠Home(Rent or EMI)",
        "💡Miscellaneous",
    ]

    while True:
        print("Select a category:")
        for index, category_name in enumerate(expense_categories, start=1):
            print(f"{index}.{category_name}")

        try:
            selected_index = int(input(f"Enter a category number [1-{len(expense_categories)}]: ")) - 1
        except ValueError:
            print("Invalid category number. Please try again.")
            continue

        if 0 <= selected_index < len(expense_categories):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount,
            )
            print(f"You have entered {expense_name} as expense name and {expense_amount} as expense amount.")
            return new_expense

        print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_name):
    print(f"💰 Saving your Expense: {expense} to {expense_file_name}")
    with open(expense_file_name, "a", encoding="utf-8") as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")


def calculate_summary(expense_file_name):
    while True:
        try:
            budget = float(input("Enter your monthly budget: "))
            if budget >= 0:
                break
            print("Budget must be zero or greater.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")

    expenses = load_expenses(expense_file_name)
    total_expense_value = sum(expense.amount for expense in expenses)
    remaining_budget = budget - total_expense_value
    remaining_budget_per_day = calculate_remaining_budget_per_day(budget, total_expense_value)

    print(f"💰 Total Expense Value is ${total_expense_value:.2f}")
    print(f"💵 Remaining Budget is ${remaining_budget:.2f}")
    print(f"📅 Remaining Budget per Day is ${remaining_budget_per_day:.2f}")

    show_category_summary(expenses)


def load_expenses(expense_file_name) -> List[Expense]:
    expenses: List[Expense] = []

    try:
        with open(expense_file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No expense file found. Starting with zero expenses.")
        return expenses

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        parts = stripped_line.split(",")
        if len(parts) != 3:
            print(f"Skipping invalid line: {line.strip()}")
            continue

        expense_name, expense_amount, expense_category = parts

        try:
            expense_amount = float(expense_amount)
        except ValueError:
            print(f"Skipping invalid amount in line: {line.strip()}")
            continue

        expenses.append(
            Expense(name=expense_name, category=expense_category, amount=expense_amount)
        )

    return expenses


def show_category_summary(expenses: List[Expense]):
    category_totals: Dict[str, float] = {}

    for expense in expenses:
        category_totals[expense.category] = category_totals.get(expense.category, 0.0) + expense.amount

    print("\n📊 Category-wise Summary:")
    for category, total in category_totals.items():
        print(f"  - {category}: ${total:.2f}")


def calculate_remaining_budget_per_day(budget, total_expense_value):
    days_in_month = calendar.monthrange(datetime.now().year, datetime.now().month)[1]
    remaining_budget = budget - total_expense_value
    remaining_budget_per_day = remaining_budget / days_in_month
    print(green_text(f"✅ Remaining Budget per Day is ${remaining_budget_per_day:.2f}"))
    return remaining_budget_per_day


def green_text(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()